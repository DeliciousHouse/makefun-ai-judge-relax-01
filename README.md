# makefun-ai-judge-relax-01

Entry for the [ai-judge-relax-01](https://make.fun/bounty/ai-judge-relax-01) relaxation text contest.

[![Contest](https://make.fun/badge/ai-judge-relax-01.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![Rank](https://make.fun/badge/ai-judge-relax-01/DeliciousHouse/makefun-ai-judge-relax-01/rank.svg)](https://make.fun/bounty/ai-judge-relax-01)
[![Reward](https://make.fun/badge/ai-judge-relax-01/DeliciousHouse/makefun-ai-judge-relax-01/reward.svg)](https://make.fun/bounty/ai-judge-relax-01)

## Output contract

`main.py` writes a single UTF-8 file `entry.txt` (1–1000 Unicode code points, nonblank, deterministic) to the directory specified by `MAKEFUN_OUTPUT_DIR`, defaulting to `/output`.

## Run

```bash
MAKEFUN_OUTPUT_DIR=./out python main.py
cat ./out/entry.txt
```

## Test

```bash
python test_entry.py
```

Tests verify the file exists, is valid UTF-8, is 1–1000 code points, is nonblank, is deterministic across two runs, and that the default output directory is `/output`.

## Requirements

Python 3.13+ standard library only. No network access.

## License

MIT
