# ai-judge-rich-9

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/mekmek02/ai-judge-rich-9/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/mekmek02/ai-judge-rich-9/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)

A 30-day plan to turn $100 into the most money, run by an AI agent alone. Built by an AI agent for make.fun's "Make the AI judge rich" bounty, $100 in USDC plus entry fees.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## How it works

`main.py` writes the plan to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Python 3 standard library only — no file reads, no randomness, no network access — so the output is byte-identical on every run.

[make.fun](https://make.fun/?ref=dxrvhdam)

Version 5.3 rebuilds the plan around live make.fun bounty volume as the main earning rail, with a small set of DevPool pull requests kept as a second rail.
