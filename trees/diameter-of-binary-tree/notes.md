# Diameter of Binary Tree

**Problem:** Given the root of a binary tree, return the length of its *diameter* — the number of edges on the longest path between any two nodes. The path need not pass through the root.

**Links:** [NeetCode](https://neetcode.io/problems/diameter-of-binary-tree) · [LeetCode 543](https://leetcode.com/problems/diameter-of-binary-tree/)

---

## My Solution — Post-order DFS with a running max

The diameter through any node equals the height of its left subtree plus the height of its right subtree (in edges). A post-order DFS returns each subtree's *height* and, on the way back up, updates a shared maximum with `left + right` before returning `1 + max(left, right)`.

| | |
|---|---|
| **Time** | O(n) — each node is visited exactly once, one height computation per node |
| **Space** | O(h) — recursion stack holds one frame per level (O(log n) balanced, O(n) worst case) |

**Caveat:** `self.res` mutates instance state rather than being scoped to the call. Harmless when the method is invoked once per instance (the LeetCode harness creates a fresh `Solution` each time), but if the same instance is reused the previous answer leaks into the new call — reset `self.res = 0` at the top or use a local variable/`nonlocal` (see optimal).

## Optimal Solution — Clean post-order DFS (`nonlocal`)

Same algorithm, with the accumulator scoped to the call instead of the object:

```python
best = 0
def height(node):
    nonlocal best
    if not node: return 0
    left, right = height(node.left), height(node.right)
    best = max(best, left + right)
    return 1 + max(left, right)
height(root)
return best
```

Asymptotically identical to my version — O(n) time, O(h) space — but safe to call repeatedly and free of hidden instance state.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(h) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + running max (optimal) | **O(n)** | **O(h)** | **Default answer** — single pass, minimal space |
| BFS/DFS to precompute all heights → scan pairs | O(n) | O(n) | Unnecessary here; recomputes heights |
| Longest-path DP (same as DFS) | O(n) | O(h) | What the optimal already is |

**Interview answer:** “Post-order DFS returning height, tracking `left + right` as the best diameter seen — O(n) time, O(h) space.” Mention the diameter is *edges*, so `left + right` (not `+1`) is the key detail.

## Edge Cases

- **Empty tree** → `0`.
- **Single node** → `0` (no edges).
- **Two nodes (root + one child)** → `1`.
- **Straight chain (n nodes)** → `n - 1`.
- **Perfectly balanced tree** → diameter = 2 × height; `left + right` at the root is maximal there.
- **Unbalanced / deep left-heavy tree** → diameter may pass through a node far from the root, which the running-max handles.
- **Diameter path through root** vs. **deeper off-path node** → both captured by `max(self.res, left + right)` at every node.