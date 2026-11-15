# Balanced Binary Tree

**Problem:** Return `True` if the tree is *height-balanced* — every node's left and right subtree heights differ by at most 1 — otherwise `False`.

**Links:** [NeetCode](https://neetcode.io/problems/balanced-binary-tree) · [LeetCode 110](https://leetcode.com/problems/balanced-binary-tree/)

---

## My Solution — Post-order DFS returning `[balanced, height]`

A post-order DFS returns a pair per subtree: `[is_balanced, height]`. A node is balanced iff both children are balanced **and** `abs(left_height - right_height) <= 1`; on failure it short-circuits by returning `[False, 0]`. The answer is the flag of the root's pair.

| | |
|---|---|
| **Time** | O(n) — each node visited once; once `False` is seen, that flag propagates up without recomputation |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) worst-case chain |

**Caveat:** `left, right = dfs(root.left), dfs(root.right)` computes **both** children before checking anything, so the right subtree is fully walked even when the left already reported unbalanced. Still O(n) total (each node once), but the sentinel version below can stop mid-subtree. Also allocates a 2-element list per node.

## Optimal Solution — Height with a `-1` sentinel

Same post-order shape, but return just the **height**, using `-1` as an "unbalanced" marker. If either child returns `-1` (or the height gap exceeds 1), propagate `-1` immediately — pruning the rest of that subtree.

| | |
|---|---|
| **Time** | O(n) worst case; prunes siblings of an unbalanced subtree |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) worst-case chain |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS with `-1` sentinel | **O(n)** | **O(h)** | **Default answer** — no per-node allocation, early prune |
| DFS returning `[balanced, height]` | O(n) | O(h) | Perfectly fine; flag+height is arguably easier to explain |
| Top-down: `abs(h(left)-h(right))<=1` at every node via standalone height calls | O(n²) | O(h) | Never — recomputes subtree heights at every level |

**Interview answer:** “Post-order DFS that returns height, propagating `-1` as an unbalanced marker; O(n) time, O(h) space.” If asked to simplify, mention the pair-returning variant is the same idea.

## Edge Cases

- **Empty tree** → `True` (base case returns balanced).
- **Single node** → `True`.
- **Chain of 2 nodes** (root + one child) → `True` (height diff 1 ≤ 1).
- **Chain of 3+ nodes** (root → left → left) → `False` (diff 2 at the root's child).
- **Perfectly balanced tree** → `True` at every node.
- **Balanced at the root but unbalanced deeper** → caught by the flag propagation, not just the root check.