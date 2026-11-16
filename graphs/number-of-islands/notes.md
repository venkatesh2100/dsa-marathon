# Number of Islands

**Problem:** Given an `m × n` grid of `"1"` (land) and `"0"` (water), count the islands — connected groups of land cells, connected horizontally or vertically (not diagonally).

**Links:** [NeetCode](https://neetcode.io/problems/count-number-of-islands) · [LeetCode 200](https://leetcode.com/problems/number-of-islands/)

---

## My Solution — Recursive DFS flood-fill, sink in place

Scan every cell; on the first unsunk `"1"` that's a new island — increment `count` and DFS from it. Each call validates the cell (bounds → not water), sinks it by writing `"0"`, and recurses into the 4 neighbors. Sinking in place both marks visited and guarantees termination without a separate `visited` set: by the time the scan reaches the island again it's all water, so each island is counted exactly once.

| | |
|---|---|
| **Time** | O(m · n) — each land cell is sunk at most once and probed by ≤ 4 neighbors; the outer scan touches every cell once |
| **Space** | O(m · n) — recursion depth is one frame per land cell in the worst case (one giant island) |

**Caveat:** Python's default recursion limit (~1000) can be hit on large single-island grids — a 100×100 all-land grid recurses ~10⁴ deep. LeetCode's tests happen to let it pass, but the robust fixes are `sys.setrecursionlimit` or going iterative. Also destroys the input grid (fine — only the count is returned), and `col = len(grid[0])` assumes a non-empty grid (LeetCode guarantees `m, n ≥ 1`).

## Optimal Solution — BFS flood-fill with a deque

Same scan + flood-fill, but the island is sunk level-by-level with an explicit queue instead of the call stack: sink the source, enqueue it, then pop a cell and enqueue its unsunk land neighbors — sinking each **when enqueued**, so a cell can never enter the queue twice. No recursion, no depth limit.

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(min(m, n)) — the BFS wavefront on a grid is a diagonal band; vs O(m · n) for the recursive DFS stack |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| BFS flood-fill (optimal) | O(m · n) | O(min(m, n)) | **Default answer** — no recursion-limit risk |
| Recursive DFS + in-place sink (my solution) | O(m · n) | O(m · n) stack | Fine for small grids / when asked for DFS explicitly |
| DFS/BFS + separate visited set | O(m · n) | O(m · n) | When the grid must not be mutated |
| Union-Find | O(m · n · α) | O(m · n) | Overkill for a one-shot count; wins for dynamic island queries (LeetCode 305) |

**Interview answer:** "Scan the grid; every unsunk land cell starts a flood-fill that marks the entire connected component as visited (sink in place) and counts it. O(m·n) time; O(min(m,n)) BFS queue or O(m·n) worst-case DFS stack."

## Edge Cases

- **Empty grid** → not a LeetCode input (`m, n ≥ 1`); my version would crash on `len(grid[0])`, the optimal guards it.
- **All water** → 0; the scan never fires a flood-fill.
- **All land** → 1; one flood-fill sinks everything.
- **Diagonal land** (`[["1","0"],["0","1"]]`) → 2 islands — diagonal does **not** connect.
- **Single row / column** → each contiguous run of `"1"` is one island.
- **Huge single island (snake shape)** → recursion depth O(m·n); use BFS.
