# Surrounded Regions

**Problem:** Given an `m × n` board of `"X"` and `"O"`, capture every region of `"O"`s that is completely surrounded by `"X"`s — flip those cells to `"X"` in place. An `"O"` on the border, or connected (4-directionally) to a border `"O"`, is safe and stays `"O"`. Returns nothing; the mutation is the output.

**Links:** [NeetCode](https://neetcode.io/problems/surrounded-regions) · [LeetCode 130](https://leetcode.com/problems/surrounded-regions/)

---

## My Solution — Border-seeded BFS + a "safe" set

Hunting enclosed regions directly is awkward — you don't know a region is surrounded until you've walked its whole perimeter. So invert the problem: a cell is captured **iff** its region never touches the border. Seed a BFS with **every border `"O"` at once**, flood through `"O"`s marking them in `vis`, then one final pass flips every `"O"` **not** in `vis` to `"X"`. The flood reaches exactly the safe cells; everything left over is enclosed.

| | |
|---|---|
| **Time** | O(m · n) — each cell enqueued at most once, probed by ≤ 4 neighbors, plus one final pass |
| **Space** | O(m · n) — `vis` set + queue |

**Caveat:** The border seeds are found by scanning the whole `m × n` grid with a four-way `or` border test inside — same complexity as scanning just the border rows/columns, but the condition reads fussy. And the `vis` set is redundant: the board can mark itself (see optimal).

## Optimal Solution — Same BFS, the board marks itself

Identical border-seeded BFS, but safe cells are stamped with a sentinel `"#"` on the grid itself (at **enqueue** time, so each cell is queued exactly once) instead of being tracked in `vis`. The sentinel is safe because inputs only ever contain `"X"`/`"O"`. Final pass over the board: leftover `"O"` → `"X"` (never touched the border — captured), `"#"` → `"O"` (border-connected — restored).

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(m · n) worst-case queue; no extra set — the grid is the visited set |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Border BFS + sentinel marking (optimal) | O(m · n) | O(m · n) queue | **Default answer** — no extra set, board restores itself |
| Border BFS + `vis` set (my solution) | O(m · n) | O(m · n) | Works; the set is redundant bookkeeping |
| DFS from border `"O"`s | O(m · n) | O(m · n) | Same idea recursively, but Python's ~1000 recursion limit dies on a 40,000-cell snake path unless raised — BFS is safer |
| Test each region for border contact | O(m · n) | O(m · n) | Awkward — must walk a whole region before knowing it's enclosed, then remember it; the inversion avoids all that |

**Interview answer:** "Flip the problem — a region is captured iff it never touches the border. Multi-source BFS from every border `"O"`, stamping reached cells with a `#` sentinel on the grid; then one pass flips leftover `"O"` → `"X"` and restores `#` → `"O"`. O(m·n) time, O(m·n) space, in place."

## Edge Cases

- **Single cell** (`[["O"]]`, `[["X"]]`) → it's a border cell → never captured.
- **Single row/column** → every cell is a border cell → nothing flips.
- **All `"O"`** → everything touches the border → board unchanged.
- **Enclosed ring around an `"X"` pillar** → the ring is one connected region, all of it flips.
- **Diagonal-only contact doesn't save a region** — flow is 4-directional, so a region diagonally adjacent to a border `"O"` is still captured.
- **All `"X"`** → no seeds, final pass flips nothing.
- **Empty grid** → not a valid input (`m, n ≥ 1`); the code would crash on `board[0]` of `[]`.
