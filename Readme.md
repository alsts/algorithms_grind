# Algorithm Grind

NeetCode 150 in Python. Part of the 8-week interview sprint (28 Sep – 22 Nov 2026). The day-by-day plan lives in the Obsidian vault: *Interview Sprint — 8-Week Plan*.

## Setup

```bash
uv sync
```

## Daily loop

```bash
uv run new.py              # scaffold the next problem in roadmap order
uv run new.py 42           # or by number / slug: uv run new.py two-sum
uv run pytest neetcode150/01_arrays_hashing/001_contains_duplicate.py
```

1. Open the NeetCode link in the file header and read the problem. Don't watch the video yet.
2. Fill in the *say it out loud first* block: brute force, then optimal, then complexity.
3. Paste the method signature + examples as tests, then solve. **Cap: 20 min on easies, 30 min on mediums.**
4. Stuck at the cap → watch the NeetCode video, then write the code yourself. Mark 🔴.
5. Put the minutes and result in the header, and tick the problem off in the vault's *NeetCode 150 Tracker*.

## Retests (Sundays)

```bash
uv run new.py 42 --retest   # blank copy in retest/, solve it blind
```

Every 🔴 gets a blind retest within 7 days.

## Layout

| Path | What |
|---|---|
| `neetcode150/NN_topic/NNN_problem.py` | This sprint's solutions, one per problem |
| `retest/` | Blind re-solves, dated |
| `problems.py` | The 150 in NeetCode roadmap order |
| `archive_2024/` | First attempt (2024): 13 problems. Re-read them the weekend before Week 1 as a warm-up, then re-solve them from scratch in Week 1 |
