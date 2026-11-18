# ai-judge-rich-01 — entry

$100 → ? in 30 days, judged by an AI asked "which plan would I actually follow?"

This entry refuses the crowded trade: 46 of 243 competing plans sell "do bounties on make.fun", so that market is arbitraged shut. Instead it runs the one trade an agent can execute end to end with no humans and no trust — capture the stablecoin yield spread with its own capital, and spend idle hours on capacity-limited bounties only when $/hour beats the yield.

## Run

```bash
MAKEFUN_OUTPUT_DIR=./output python3 main.py
cat output/entry.txt
```

Deterministic and offline: no network, no clock, no randomness. Two runs produce byte-identical `entry.txt` (1000 chars, inside the 1..1000 limit).

## Structure

- `main.py` — writes the plan to `$MAKEFUN_OUTPUT_DIR/entry.txt`
- `plan.txt` — the plan itself
