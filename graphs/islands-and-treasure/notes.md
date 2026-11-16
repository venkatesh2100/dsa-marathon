# Islands and Treasure (Walls and Gates)

**Problem:** Given an `m × n` grid where `-1` = wall, `0` = gate, and `2147483647` (INF) = empty room, fill each empty room **in place** with the distance to its *nearest* gate. Rooms that can't reach any gate stay INF. Returns nothing — the mutation is the output.

**Links:** [NeetCode](https://neetcode.io/problems/islands-and-treasure) · [LeetCode 286](https://leetcode.com/problems/walls-and-gates/) (premium)

---

## My Solution — Multi-source BFS, level snapshots

Seed the queue with **every gate at once** and BFS level-by-level: pop the whole current level, write `dis` into every unfilled neighbor, then `dis += 1` for the next level. A `vis` set guards against revisits (gates are seeded into it too, so they're never overwritten).

Why one BFS from all gates works instead of one per gate: BFS explores in rings of increasing distance, so from the merged multi-source wavefront, the **first** fill a room receives is necessarily from its closest gate — later (longer) paths arrive after the cell is already marked. One pass, O(m·n), instead of O((m·n)²) for per-gate BFS.

| | |
|---|---|
| **Time** | O(m · n) — each cell enters the queue at most once; each cell is probed by ≤ 4 neighbors |
| **Space** | O(m · n) — `vis` set + queue (all gates can be seeded at once) |

**Caveat:** The `vis` set is redundant — a filled cell is recognizable by its value: only cells still equal to INF are fillable, and gates (`0`) and walls (`-1`) fail the fill test anyway. Dropping the set removes a hash add/probe per cell. (Same recursion-free style as the BFS habit from the island problems — no stack-depth worries here at all.)

## Optimal Solution — Same BFS, the grid marks itself

Identical multi-source BFS, but the `vis` set is gone: a cell is filled **iff** it's still INF. Gates and walls are skipped because they're not INF, filled cells are skipped because they've been overwritten with `dis ≥ 1`. Unreachable rooms are never touched, so they correctly stay INF.

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(m · n) worst case — the queue can hold every gate seed at once (no single-source wavefront bound here) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Multi-source BFS, grid-as-visited (optimal) | O(m · n) | O(m · n) queue | **Default answer** — no set bookkeeping |
| Multi-source BFS + `vis` set (my solution) | O(m · n) | O(m · n) | Works; the set is redundant but harmless |
| BFS from each gate separately | O((m · n)²) | O(m · n) | Never — unless asked "what if you BFS per gate?" as a stepping stone |
| DFS from each gate | O(m · n) possible but subtle | O(m · n) | Risky — must allow re-visits when a shorter path appears; easy to get wrong |

**Interview answer:** "Multi-source BFS from all gates simultaneously — seed them all at distance 0, fill each empty room the first time the wavefront reaches it (that first fill is the shortest distance by BFS ordering), never revisit. O(m·n) time and space."

## Edge Cases

- **No gates** → queue starts empty; every room stays INF.
- **Room sealed behind walls** (`[[0,-1],[-1,INF]]`) → stays INF; the wavefront never reaches it.
- **All gates** (`[[0,0],[0,0]]`) → all seeds, nothing to fill; grid unchanged.
- **Single cell** (`[[0]]` or `[[INF]]`) → unchanged.
- **Single row / column** → distances count steps left/right or up/down.
- **Empty grid** → not a LeetCode input (`m, n ≥ 1`); my version would crash on `len(grid[0])`, the optimal guards it.
