# Maximum Depth of Binary Tree

**Problem:** Return the number of nodes along the longest path from the root down to the farthest leaf (the tree's height).

**Links:** [NeetCode](https://neetcode.io/problems/depth-of-binary-tree) · [LeetCode 104](https://leetcode.com/problems/maximum-depth-of-binary-tree/)

---

## My Solution — Breadth-first (level-order) traversal

Run BFS with a queue. Process one whole level at a time by snapshotting `len(que)` before the inner loop, then increment `ans` once per level completed. When the queue drains, `ans` equals the number of levels — which is exactly the maximum depth.

| | |
|---|---|
| **Time** | O(n) — every node is enqueued and dequeued once |
| **Space** | O(w) — queue holds the widest level `w`; O(n/2) for a full tree, O(1) for a chain |

**Caveat:** Space scales with the *widest level*, not the height. For a balanced/full tree that is ~n/2 nodes sitting in the queue at once, whereas a DFS on the same tree only ever holds the height. The `for i in range(len(que))` snapshot is also easy to get subtly wrong if `len(que)` is re-evaluated (queue shrinks mid-loop → levels merge).

## Optimal Solution — Recursive DFS

A tree's depth is one plus the deeper of its two subtrees, with an empty subtree contributing 0:

```python
return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
```

Every node is visited once and the answer is computed on the way back up the call stack — no extra data structure needed.

| | |
|---|---|
| **Time** | O(n) — each node visited exactly once |
| **Space** | O(h) — call stack holds one frame per level; O(log n) balanced, O(n) fully skewed |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Recursive DFS | **O(n)** | **O(h)** | **Default answer** — shortest, and best space on balanced trees |
| Iterative BFS (my solution) | O(n) | O(w) ≤ O(n) | Height/skew worries (no recursion limit); or when you already need level-order anyway |
| Iterative DFS (explicit stack of `(node, depth)`) | O(n) | O(h) | Same space profile as recursion without the stack-overflow risk |

**Interview answer:** “`1 + max(depth(left), depth(right))`, O(n) time and O(h) space on the call stack.” Mention BFS as the level-order alternative if recursion depth is a concern.

## Edge Cases

- **Empty tree** → `0` (base case; my BFS returns `0` before the queue even runs).
- **Single node** → `1`.
- **Only a left chain / only a right chain** → depth `= n`; recursion uses O(n) stack here (fine at interview sizes, flag it for huge inputs).
- **Perfectly balanced tree** → depth `= log2(n) + 1`; BFS queue peaks at ~n/2 nodes.
- **Uneven tree** (one deep branch, one stub) → `max` correctly follows the deeper side.
