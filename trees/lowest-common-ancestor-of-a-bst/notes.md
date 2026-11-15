# Lowest Common Ancestor of a Binary Search Tree

**Problem:** Given a BST and two nodes `p`, `q` that both exist in it, return their lowest common ancestor — the deepest node that has both as descendants (a node may be its own ancestor).

**Links:** [NeetCode](https://neetcode.io/problems/lowest-common-ancestor-in-binary-search-tree) · [LeetCode 235](https://leetcode.com/problems/lowest-common-ancestor-of-a-bst/)

---

## My Solution — Recursive BST descent

Exploit the BST ordering: if both targets are strictly smaller than the current node, the LCA is in the left subtree; if both strictly larger, in the right; otherwise the paths diverge here (or the node *is* one of the targets) — return it.

| | |
|---|---|
| **Time** | O(h) — one root-to-split walk; O(log n) balanced, O(n) skewed chain |
| **Space** | O(h) — one recursion frame per level descended |

**Caveat:** No null guard: `root.val` is dereferenced every call. Safe *only* because LC guarantees both nodes exist — the walk can never run past the split point. If p or q could be missing, an iterative guard or a validity check is required, or it crashes with `AttributeError` on `None`.

## Optimal Solution — Iterative descent, O(1) space

Same walk without recursion: keep a `cur` pointer, move it left/right while both targets sit on the same side, return it the moment they split.

| | |
|---|---|
| **Time** | O(h) — same single descent |
| **Space** | **O(1)** — no call stack, just the pointer |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Iterative descent | **O(h)** | **O(1)** | **Default answer** — trivially converts, no stack cost |
| Recursive descent (my solution) | O(h) | O(h) stack | Fine; identical logic, one extra frame per level |
| General-tree LCA (recurse both subtrees) | O(n) | O(h) | Only for a *plain* binary tree (LC 236), where ordering can't guide the walk |

**Interview answer:** “BST property does the work: walk down while both targets are on the same side; the first node where they split — or that equals one of them — is the LCA. O(h) time, O(1) space iteratively.”

## Edge Cases

- **p == q** → that node itself (returns immediately at the root).
- **p or q is the root** → the root (equal values hit the `else` branch).
- **p is an ancestor of q** → the ancestor node (walk stops when cur becomes p).
- **Targets in opposite subtrees** → split at the first divergent node, typically near the root.
- **Skewed chain** → O(n) time; recursion also uses O(n) stack (iterative stays O(1)).
- **Values equal to node values en route** → handled by strict `<`/`>`: equality forces the `else` branch, correctly stopping.