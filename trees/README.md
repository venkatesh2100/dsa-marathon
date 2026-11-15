# Binary Trees

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Maximum Depth of Binary Tree](max-depth-of-binary-tree/) | Recursive DFS | O(n) | O(h) | `1 + max(depth(left), depth(right))`; every node once, stack holds the height |
| [Invert Binary Tree](invert-binary-tree/) | Recursive DFS (in-place) | O(n) | O(h) | Swap children at every node recursively; O(h) stack space; BFS alternative costs O(w) queue space (w = widest level) |
| [Diameter of Binary Tree](diameter-of-binary-tree/) | Post-order DFS + running max | O(n) | O(h) | Track `left + right` at every node as candidate diameter while returning heights |
| [Balanced Binary Tree](balanced-binary-tree/) | Post-order DFS, `-1` sentinel | O(n) | O(h) | Return height or `-1` if unbalanced; prunes siblings once `False` is known |
| [Same Tree](same-tree/) | Recursive DFS pair comparison | O(n) | O(h) | Both `None` → match; one `None` or value mismatch → fail; recurse on both subtrees with short-circuit `and` |
| [Subtree of Another Tree](subtree-of-another-tree/) | DFS + same-tree check per node | O(n · m) | O(n + m) | Same-Tree comparison at every node of root, recurse left/right on failure; O(n + m) follow-up: serialize with null markers + substring search |
| [Lowest Common Ancestor of a BST](lowest-common-ancestor-of-a-bst/) | Iterative descent on BST order | O(h) | O(1) | Walk down while both targets are on the same side; return at the split point or when `cur` is `p`/`q`; no null guard needed only because targets are guaranteed present |
