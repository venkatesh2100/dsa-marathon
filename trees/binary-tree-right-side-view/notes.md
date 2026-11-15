# Binary Tree Right Side View

**Problem:** Return the values of the nodes visible when looking at the binary tree from the right side — the rightmost node of each level, top to bottom.

**Links:** [NeetCode](https://neetcode.io/problems/binary-tree-right-side-view) · [LeetCode 199](https://leetcode.com/problems/binary-tree-right-side-view/)

---

## My Solution — BFS, keep the last value per level

Level-order BFS with the standard per-level snapshot; within each level, overwrite `val` for every node processed, so when the level ends `val` holds the rightmost node's value. Append it once per level.

| | |
|---|---|
| **Time** | O(n) — each node dequeued exactly once |
| **Space** | O(w) — queue holds the widest level (up to ~n/2 in a full tree) |

**Caveat:** The `val = 0` reset and the `if node:` guard are both dead code — the queue is never empty mid-level and never contains `None` (children are appended only when truthy). They're harmless here, but `val = 0` would actively produce a wrong `0` row if a level ever *were* empty; the guard is what papers over that risk.

## Optimal Solution — Right-first DFS with depth check

Traverse depth-first **right child first**, tracking depth. The first node ever reached at each new depth is, by construction, the rightmost node of that level — record it once: `if depth == len(res): res.append(node.val)`.

| | |
|---|---|
| **Time** | O(n) — each node visited once |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) chain; no queue needed |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Right-first DFS | **O(n)** | **O(h)** | **Default answer** — no queue, one `len(res)` check |
| BFS last-in-level (my solution) | O(n) | O(w) | Fine; natural if you already have level-order scaffolding |
| BFS + explicit level-size loop keeping index | O(n) | O(w) | Same as mine, more bookkeeping |

**Interview answer:** “DFS going right-first; whenever depth equals the number of rows seen so far, this is the level's rightmost node — append it. O(n) time, O(h) space.”

## Edge Cases

- **Empty tree** → `[]`.
- **Single node** → `[val]`.
- **Perfect tree** → rightmost path only (`[root, right, right, ...]`).
- **Left-leaning chain** → right view is the *whole* chain — every level's only node is its leftmost, which is also its rightmost (`[1,2,3,4]`).
- **Missing right child mid-tree** (`[1,2,3,None,5,None,4]`) → level 2's rightmost is `5`, not `4` — the case that breaks any "just follow right pointers" shortcut.
- **Deep skew** → DFS recursion O(n) stack (flag for huge inputs); BFS queue also O(n) on a chain.