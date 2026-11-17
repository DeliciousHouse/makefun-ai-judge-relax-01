"""Tests for the relaxation contest entry."""

import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


class TestEntry(unittest.TestCase):

    def _run_main(self, output_dir):
        """Run main.py in a subprocess with MAKEFUN_OUTPUT_DIR set."""
        env = os.environ.copy()
        env["MAKEFUN_OUTPUT_DIR"] = output_dir
        result = subprocess.run(
            [sys.executable, "main.py"],
            env=env,
            capture_output=True,
            timeout=30,
        )
        self.assertEqual(result.returncode, 0,
                         f"main.py failed:\n{result.stderr.decode()}")
        return os.path.join(output_dir, "entry.txt")

    def test_output_exists(self):
        with tempfile.TemporaryDirectory(dir=REPO_DIR) as td:
            path = self._run_main(td)
            self.assertTrue(os.path.isfile(path), "entry.txt not created")

    def test_utf8_and_length(self):
        with tempfile.TemporaryDirectory(dir=REPO_DIR) as td:
            path = self._run_main(td)
            with open(path, "rb") as f:
                raw = f.read()
            text = raw.decode("utf-8")
            codepoints = len(text)
            self.assertGreaterEqual(codepoints, 1, "entry is empty")
            self.assertLessEqual(codepoints, 1000,
                                 f"entry too long: {codepoints} code points")

    def test_nonblank(self):
        with tempfile.TemporaryDirectory(dir=REPO_DIR) as td:
            path = self._run_main(td)
            with open(path, "rb") as f:
                raw = f.read()
            text = raw.decode("utf-8")
            self.assertTrue(text.strip(), "entry is blank")

    def test_deterministic(self):
        with tempfile.TemporaryDirectory(dir=REPO_DIR) as td1, \
             tempfile.TemporaryDirectory(dir=REPO_DIR) as td2:
            path1 = self._run_main(td1)
            path2 = self._run_main(td2)
            with open(path1, "rb") as f1, open(path2, "rb") as f2:
                self.assertEqual(f1.read(), f2.read(),
                                 "outputs differ between runs")

    def test_default_output_dir(self):
        """With MAKEFUN_OUTPUT_DIR absent, main() writes to /output/entry.txt."""
        import main as m
        env_without = {k: v for k, v in os.environ.items()
                       if k != "MAKEFUN_OUTPUT_DIR"}
        with patch.dict(os.environ, env_without, clear=True), \
             patch("main.pathlib.Path") as mock_path_cls:
            m.main()
        mock_path_cls.assert_called_with("/output")
        dest = mock_path_cls.return_value
        dest.mkdir.assert_called_once_with(parents=True, exist_ok=True)
        dest.__truediv__.assert_called_once_with("entry.txt")
        dest.__truediv__.return_value.write_text.assert_called_once_with(
            m.ENTRY, encoding="utf-8"
        )


if __name__ == "__main__":
    unittest.main()
