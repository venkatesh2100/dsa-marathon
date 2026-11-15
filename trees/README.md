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
| [Binary Tree Level Order Traversal](binary-tree-level-order-traversal/) | BFS with per-level queue snapshot | O(n) | O(w) | Inner `for _ in range(len(q))` processes exactly one level; DFS + depth-indexed buckets is the no-queue alternative |
| [Binary Tree Right Side View](binary-tree-right-side-view/) | Right-first DFS, one row per depth | O(n) | O(h) | First node reached at each new depth is that level's rightmost; BFS alternative keeps the last value per level at O(w) queue cost |
| [Count Good Nodes in Binary Tree](count-good-nodes-in-binary-tree/) | DFS passing path max down | O(n) | O(h) | Node counts itself if `val >= max-so-far`; ties are good (`>=`, not `>`); BFS tuple version costs O(w) queue space |
