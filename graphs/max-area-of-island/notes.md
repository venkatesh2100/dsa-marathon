# Max Area of Island

**Problem:** Given an `m × n` binary grid of `1` (land) and `0` (water), return the maximum **area** of an island — the number of cells in the largest 4-directionally connected group of land cells.

**Links:** [NeetCode](https://neetcode.io/problems/max-area-of-island) · [LeetCode 695](https://leetcode.com/problems/max-area-of-island/)

---

## My Solution — Recursive DFS with a `nonlocal` counter

Same flood-fill shape as Number of Islands: scan the grid, and on the first unsunk `1` run a DFS that sinks each land cell (`grid[r][c] = 0`) and increments a shared counter `val`. `val` is reset to 0 before each island's DFS; after it drains the island, `res = max(res, val)` keeps the running best.

| | |
|---|---|
| **Time** | O(m · n) — each land cell is sunk at most once and probed by ≤ 4 neighbors; the scan touches every cell once |
| **Space** | O(m · n) — recursion depth is one frame per land cell of the largest island (worst case: the whole grid) |

**Caveat:** The mutable counter + reset pattern is easy to fumble — forget `val = 0` and every island reports a *cumulative* total, which still passes on `[[1]]`-style tests and quietly returns the total land area on multi-island ones. A cleaner variant has `dfs` *return* the area: `return 1 + dfs(r±1, c±1)` summed over the 4 neighbors. Same recursion-limit risk as always (O(m·n) deep on a huge single island), destroys the input grid, and `len(grid[0])` assumes a non-empty grid (LeetCode guarantees `m, n ≥ 1`).

## Optimal Solution — BFS flood-fill with a deque

Identical scan + flood-fill, but each island is drained level-by-level with an explicit queue instead of the call stack: sink the source, enqueue it, then pop a cell (count it — it enters the queue exactly once) and enqueue its unsunk land neighbors, sinking each **when enqueued** so nothing is ever counted twice. No recursion, no depth limit, no shared mutable counter to reset.

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(min(m, n)) — the BFS wavefront on a grid is a diagonal band; vs O(m · n) for the recursive DFS stack |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| BFS flood-fill (optimal) | O(m · n) | O(min(m, n)) | **Default answer** — no recursion-limit risk, no mutable counter |
| Recursive DFS returning area | O(m · n) | O(m · n) stack | When asked for DFS — cleaner than a `nonlocal` counter, same depth risk |
| Recursive DFS + `nonlocal` counter (my solution) | O(m · n) | O(m · n) stack | Works; reset-per-island is a correctness footgun |
| Union-Find | O(m · n · α) | O(m · n) | Overkill; wins only for dynamic island variants |

**Interview answer:** "Flood-fill each island and count its cells, tracking the max. Same sink-in-place trick as Number of Islands: O(m·n) time; O(min(m,n)) BFS queue or O(m·n) worst-case DFS stack. In Python I'd go BFS to dodge the recursion limit."

## Edge Cases

- **Empty grid** → not a LeetCode input; my version would crash on `len(grid[0])`, the optimal guards it.
- **All water** → 0; no DFS ever fires.
- **All land** → m · n; one flood-fill covers everything.
- **Diagonal land** (`[[1,0],[0,1]]`) → 1 — diagonal does **not** connect.
- **Single row / column** → largest contiguous run of `1`s.
- **Single cell** → 1 or 0.
- **Huge single island (snake shape)** → recursion depth O(m·n); use BFS.
- **Counter reset bug** → `[["1","0","1"]]` returns 2 (cumulative) instead of 1 if `val = 0` is dropped.
