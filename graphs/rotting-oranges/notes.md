# Rotting Oranges

**Problem:** Given an `m × n` grid of `0` (empty), `1` (fresh orange), `2` (rotten orange), every minute rot spreads 4-directionally to adjacent fresh oranges. Return the minutes until **no** fresh orange remains, or `-1` if some fresh orange can never rot.

**Links:** [NeetCode](https://neetcode.io/problems/rotting-orange) · [LeetCode 994](https://leetcode.com/problems/rotting-oranges/)

---

## My Solution — Multi-source BFS, level snapshots + visited set

Seed the queue with **every rotten orange at once** and count the fresh ones; return `0` immediately if there are none. Then BFS level-by-level: pop the current level, rot every fresh neighbor (mark it `2`, decrement `count`), and after the level drains, `res += 1`. Because `res` starts at `-1`, after the first (source) level it's `0`, and it ends up equal to the number of minutes elapsed. Finally: `count == 0` → return `res`; any fresh orange left → `-1`.

| | |
|---|---|
| **Time** | O(m · n) — each cell enters the queue at most once (rotten seeds once; each fresh cell rots exactly once) |
| **Space** | O(m · n) — `vis` set + queue (all rotten oranges can be seeded at once) |

**Caveat:** The `vis` set is *needed* here only because the fill test checks `grid[dx][dy] == 0` — that distinguishes empty from non-empty but not fresh (`1`) from rotten (`2`), so without the set a rotten cell would be re-rotted forever. Flip the test to `grid[nr][nc] == 1` (only fresh cells can rot) and the grid marks itself — rotten cells are `2` and get skipped naturally, no set. Also, `res = -1` + post-increment walks one final phantom level (the last rotted oranges sit through an extra empty iteration); same answer, just one wasted level.

## Optimal Solution — Same BFS, `== 1` test, early exit

Identical multi-source BFS, minus the set: a cell rots **iff** it's still `1`, so the grid marks itself. The loop is `while q and fresh` with the minute increment *before* each level — the moment the last fresh orange rots, the loop exits, which both removes the phantom final level and makes `res = -1` unnecessary (`minutes` just counts levels). Fresh count left nonzero → `-1`.

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(m · n) worst case — the queue can hold every rotten seed at once |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Multi-source BFS, grid-as-visited (optimal) | O(m · n) | O(m · n) queue | **Default answer** |
| Multi-source BFS + `vis` set (my solution) | O(m · n) | O(m · n) | Works; the set is only load-bearing if the fill test is `!= 0` |
| BFS from each rotten orange separately | broken / O((m · n)²) | O(m · n) | Never — later waves would overwrite earlier (shorter) times; multi-source resolves the conflict |
| DFS | — | — | Wrong tool — spread time is a *level* quantity; DFS gives order, not minutes |

**Interview answer:** "Multi-source BFS from all rotten oranges, tracking a fresh counter. Each BFS level is one minute; the first time a fresh orange is reached is its rot time. If fresh never hits zero, -1. O(m·n) time and space."

## Edge Cases

- **No fresh oranges** (`[[0,2]]`, `[[0]]`, all rotten) → `0` via the early return — not `-1`!
- **Fresh but no rotten** (`[[1]]`) → queue empty, loop never runs → `-1`.
- **Fresh orange walled off by empties** (`[[2,0,1]]`) → `-1`.
- **Chain spread** (`[[2,1,1,1]]`) → 3 — one minute per link.
- **Multiple rotten** → they spread simultaneously; a cell rots at its true distance from the *nearest* rotten orange.
- **Empty grid** → not a LeetCode input (`m, n ≥ 1`); my version would crash on `len(grid[0])`, the optimal guards it.
