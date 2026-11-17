"""Tests for the relaxation contest entry."""

import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


class TestEntry(unittest.TestCase):

    def _run_main(self, output_dir):
        """Run main.py with MAKEFUN_OUTPUT_DIR pointing to output_dir."""
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = output_dir
        result = subprocess.run(
            [sys.executable, "main.py"],
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0, f"main.py failed:\n{result.stderr}")
        return os.path.join(output_dir, "entry.txt")

    def test_output_exists(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._run_main(td)
            self.assertTrue(os.path.isfile(path), "entry.txt not created")

    def test_utf8_and_length(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._run_main(td)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            codepoints = len(text)
            self.assertGreaterEqual(codepoints, 1, "entry is empty")
            self.assertLessEqual(codepoints, 1000, f"entry too long: {codepoints} code points")

    def test_nonblank(self):
        with tempfile.TemporaryDirectory() as td:
            path = self._run_main(td)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            self.assertTrue(text.strip(), "entry is blank")

    def test_deterministic(self):
        with tempfile.TemporaryDirectory() as td1, tempfile.TemporaryDirectory() as td2:
            path1 = self._run_main(td1)
            path2 = self._run_main(td2)
            with open(path1, "rb") as f1, open(path2, "rb") as f2:
                self.assertEqual(f1.read(), f2.read(), "outputs differ between runs")

    def test_default_output_dir(self):
        """When MAKEFUN_OUTPUT_DIR is unset, main.py targets /output.
        We verify the code path by patching — not by writing to /output."""
        env = os.environ.copy()
        env.pop("MAKEFUN_OUTPUT_DIR", None)
        # Run in a subprocess that will likely fail (no /output), but
        # capture stderr to confirm it tried the right directory.
        result = subprocess.run(
            [sys.executable, "-c",
             "import main; print(main.output_dir())"],
            env=env,
            capture_output=True,
            text=True,
            timeout=30,
        )
        # The function should return the absolute /output path
        self.assertIn("/output", result.stdout.strip().replace("\\", "/"),
                       "default output dir should be /output")


if __name__ == "__main__":
    unittest.main()
