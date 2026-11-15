# Binary Trees

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Maximum Depth of Binary Tree](max-depth-of-binary-tree/) | Recursive DFS | O(n) | O(h) | `1 + max(depth(left), depth(right))`; every node once, stack holds the height |
| [Invert Binary Tree](invert-binary-tree/) | Recursive DFS (in-place) | O(n) | O(h) | Swap children at every node recursively; O(h) stack space; BFS alternative costs O(w) queue space (w = widest level) |
| [Diameter of Binary Tree](diameter-of-binary-tree/) | Post-order DFS + running max | O(n) | O(h) | Track `left + right` at every node as candidate diameter while returning heights |
