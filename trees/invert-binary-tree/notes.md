# Invert Binary Tree

**Problem:** Given the root of a binary tree, invert it (swap left and right children at every node) and return the root.

**Links:** [NeetCode](https://neetcode.io/problems/invert-binary-tree) · [LeetCode 226](https://leetcode.com/problems/invert-binary-tree/)

---

## My Solution — Iterative BFS

Use a queue to traverse level-order. For each node popped, swap its left and right children, then enqueue any non-null children. The tree is modified in-place and the original root is returned.

| | |
|---|---|
| **Time** | O(n) — every node is visited once |
| **Space** | O(w) — queue holds the widest level `w` (up to n/2 in a full tree) |

**Caveat:** Space scales with the *widest level*, not the height. For a balanced/full tree that is ~n/2 nodes in the queue, whereas DFS only holds the height.

## Optimal Solution — Recursive DFS (in-place)

Swap children at each node, then recurse on the (now swapped) subtrees:

```python
def invert(node):
    node.left, node.right = node.right, node.left
    if node.left:  invert(node.left)
    if node.right: invert(node.right)
invert(root)
```

Every node is visited once, no auxiliary data structure, call stack depth = tree height.

| | |
|---|---|
| **Time** | O(n) — each node visited once |
| **Space** | O(h) — call stack; O(log n) balanced, O(n) worst-case chain |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Recursive DFS (optimal) | **O(n)** | **O(h)** | **Default answer** — concise, in-place, best space on balanced trees |
| Iterative BFS (my solution) | O(n) | O(w) | No recursion limit; or when you already need level-order anyway |
| Iterative DFS (explicit stack) | O(n) | O(h) | Same profile as recursion without stack-overflow risk |

**Interview answer:** “Recursively swap children at every node, O(n) time, O(h) stack space.” Mention BFS if recursion depth is a concern.

## Edge Cases

- **Empty tree** → `None` (base case; both solutions return early).
- **Single node** → tree unchanged.
- **Only left chain / only right chain** → becomes right chain / left chain; recursion uses O(n) stack here (fine at interview sizes, flag for huge inputs).
- **Perfectly balanced tree** → depth `= log2(n) + 1`; BFS queue peaks at ~n/2 nodes.
- **Tree with both children at every node** → all children swapped correctly.