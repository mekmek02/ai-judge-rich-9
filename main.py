# Runner for the AI Judge Rich v5.3 entry.
# The judge scores the text held in PLAN below, so this file does one job:
# carry that text to entry.txt byte for byte. No network, no clock, no
# randomness, no input: the same bytes come out on every run.

import os

# The entry text: eight lines, 980 characters, plain ASCII. It is the
# submission itself, so it stays exactly as written here.
PLAN = """Judge: posted-price only, paid on merge or from escrow. Fiverr, Upwork, Stripe need human ID; cold mail unread; DevPool: 61 of 79 issues over a year old, 1 outside merge since Aug.
Board: make.fun 7 open, $4,098, 5 free, 130 paid; 40 new in 7 days. Top paid $570.50 in 20 of 25, $22.82 an entry; top 50 $6.56.
Days 1-2: kit, wallet. $20 credit, $10 fees, $70 kept.
Rail 1: 3 closing soonest; 4 drafts duel under each judge, both orders, winner only; only pots settling by day 30; payouts recycle into fees.
Rail 2: DevPool /start 2 at $40-$300; outsider merged 7 days, CI green, unassigned; failing test first, PR 24h; max 2 open, stalled 5 days, drop.
Math: 100 entries, 85 settle at $11.41 $970; 10 PRs, 5 merge x $150 less 20% $600. Day 30 ~$1,640. Floor: 85 x $6.56 $558; 3 merge $360 + $70 ~$988.
Kill: type unpaid after 3, drop; under $30/hour 3 days, test-suite fixes.
Edge: money exists before I work, judge rehearsed before I enter; finished code first, escrow-paid only."""

# Refuse to emit a broken entry: the plan must fit the 1-1000 character
# window and be plain ASCII, or the judge cannot score it at all.
if len(PLAN) < 1 or len(PLAN) > 1000:
    raise SystemExit("plan must be 1-1000 characters, got %d" % len(PLAN))
try:
    PLAN.encode("ascii")
except UnicodeEncodeError:
    raise SystemExit("plan must be plain ASCII")

# The runner collects entry.txt from this folder. Make the folder when it
# is missing, then write the plan exactly as it stands: no trailing
# newline, no extra whitespace, nothing added.
target_folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(target_folder, exist_ok=True)
with open(os.path.join(target_folder, "entry.txt"), "w", encoding="ascii", newline="") as out:
    out.write(PLAN)
