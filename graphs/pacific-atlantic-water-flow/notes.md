# Pacific Atlantic Water Flow

**Problem:** Given an `m × n` grid of island heights, water can flow from a cell to an adjacent cell with height **less than or equal** to its own. Border cells touch an ocean: the top row and left column border the Pacific, the bottom row and right column border the Atlantic. Return every cell from which water can reach **both** oceans.

**Links:** [NeetCode](https://neetcode.io/problems/pacific-atlantic-water-flow) · [LeetCode 417](https://leetcode.com/problems/pacific-atlantic-water-flow/)

---

## My Solution — Two reverse BFS sweeps from the oceans

Instead of asking "can *this* cell reach an ocean?" per cell (O((m·n)²)), flip the flow: seed a BFS from **every Pacific border cell at once** and walk **uphill** (`heights[neighbor] >= heights[current]`) — every cell reached is one the Pacific can receive water from. Repeat from the Atlantic border. The answer is the **intersection** of the two visited sets. Two `que`/`vis` pairs, one per ocean, then a loop over `vis` checking membership in `vis2`.

Why reversing works: the flow rule is `neighbor ≤ current`, so descent from A to B is exactly ascent from B to A — "this cell drains to the ocean" and "this cell is reachable from the ocean border going uphill" are the same condition, and one shared BFS answers it for all cells at once.

| | |
|---|---|
| **Time** | O(m · n) — each cell enters each sweep at most once, probed by ≤ 4 neighbors; two sweeps + one intersection pass |
| **Space** | O(m · n) — two visited sets + queues |

**Caveats:**
- The corner cell (e.g. `(0,0)`) is seeded twice — once by the row loop, once by the column loop — a harmless duplicate in the queue.
- Result order is whatever set iteration yields; LeetCode accepts any order.
- The two BFS blocks are copy-paste duplicates; only the seeds differ. The optimal file factors them into one `flow_from` helper.

## Optimal Solution — Same algorithm, one BFS helper

The pasted solution is already the optimal approach. The cleanup: a single `flow_from(seeds)` runs both sweeps (Pacific seeds `[(r, 0)...] + [(0, c)...]`, Atlantic seeds mirrored), chained comparisons `0 <= dx < row and 0 <= dy < col` replace the four-clause guard, and the intersection becomes a direct set operation `pacific & atlantic` instead of a Python loop. Same O(m·n).

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(m · n) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Reverse multi-source BFS from both oceans (both files) | O(m · n) | O(m · n) | **Default answer** — no recursion-limit risk, no repeated work |
| Reverse DFS from both oceans | O(m · n) | O(m · n) | Same complexity, but Python's ~1000 recursion limit dies on a 40,000-cell snake path unless raised — BFS is safer |
| BFS from every cell toward each ocean | O((m · n)²) | O(m · n) | Never — the reverse sweep exists precisely to share that work |

**Interview answer:** "Don't test each cell against each ocean — flip the flow. Multi-source BFS from all Pacific border cells walking uphill marks everything the Pacific can reach; same from the Atlantic; the answer is the intersection of the two visited sets. O(m·n) time and space, no recursion."

## Edge Cases

- **Single cell** (`[[1]]`) → it *is* the entire border of both oceans → `[[0,0]]`.
- **Single row or column** (`[[3,1,2]]`) → every cell touches both the top/bottom (or left/right) edges → **all** cells qualify, even ones that can't move anywhere.
- **Interior moat** (`[[3,3,3],[3,1,3],[3,3,3]]`) → the center is below all four neighbors and reaches **neither** ocean → the 8 border cells only.
- **All equal heights** → flow is never blocked → every cell.
- **Local-minimum corner** (`[[1,2,3],[6,5,4],[7,8,9]]`) → `(0,0)` and `(0,1)` are surrounded by higher cells; they drain nowhere but the Pacific and are excluded.
- **Empty grid** → not a valid input (`m, n ≥ 1` per constraints); both versions would crash on `heights[0]` of `[]`.
