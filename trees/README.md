# Binary Trees

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Maximum Depth of Binary Tree](max-depth-of-binary-tree/) | Recursive DFS | O(n) | O(h) | `1 + max(depth(left), depth(right))`; every node once, stack holds the height; BFS alternative costs O(w) queue space (w = widest level, up to n/2 in a full tree) |
