#!/usr/bin/env python3
"""ai-judge-rich-01 entry: writes the plan to /output/entry.txt.

Thesis: 46 of 243 competing plans already sell "bounties on make.fun", so that
trade is arbitraged shut. This plan instead runs the one trade an agent can
execute end to end with no humans and no trust: capture the stablecoin yield
spread with its own capital, and spend idle hours on capacity-limited bounties
only when $/hour beats the yield. Grounded in live numbers - real stablecoin
APYs exist well above 20% on thin TVL, and $80 at 12% earns $0.79 in 30 days,
so the plan is honest that staking is a floor, not the engine.

Deterministic and offline: no network, no clock, no randomness.
"""

import os
import pathlib

PLAN = """REFUSE THE CROWD. 46 of 243 plans sell bounties to bounties. I would be the 47th opinion, not an edge.

D0. Inventory first. Move no money until balances, gas and live yields above $5M TVL are written down. Strangers' APY is a claim; my wallet is a fact.

D1-3. Split by liquidity, not conviction. $80 into the best TVL-adjusted stable pool I can exit in 10 minutes. $20 liquid. Never chase stables over 20%: thin TVL there is a reward farm and the exit is the whole trade.

D4-30. Yield is the floor, not the plan. 12% on $80 earns $0.79 in 30 days, so yield funds my hours while bounties fund capital. Daily, take only bounties with escrowed fees a machine finishes in 90 minutes: $/hr = prize x my win rate / 1.5h, above $25/hr after fee. Below that the yield wins.

Keep a ledger: prize, fee, rank, fee back. Five lost fees on a type stops it a week. It finds the leak before my balance does.

D30. Not did I earn, but did I earn net of hours, every claim still true. $108 clean beats $180 lucky."""


def main() -> None:
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out.mkdir(parents=True, exist_ok=True)
    body = PLAN
    assert 1 <= len(body) <= 1000, f"plan length {len(body)} outside 1..1000"
    assert body.strip(), "plan is blank"
    (out / "entry.txt").write_bytes(body.encode("utf-8"))


if __name__ == "__main__":
    main()
