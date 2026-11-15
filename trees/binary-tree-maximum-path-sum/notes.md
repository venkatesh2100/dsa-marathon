# Binary Tree Maximum Path Sum

**Problem:** Given the root of a (possibly negative-valued) binary tree, return the maximum sum obtainable by any path — a sequence of adjacent nodes where each node appears at most once, and the path need not pass through the root.

**Links:** [NeetCode](https://neetcode.io/problems/binary-tree-maximum-path-sum) · [LeetCode 124](https://leetcode.com/problems/binary-tree-maximum-path-sum/)

---

## My Solution — Post-order DFS with a "gain" return

Two different quantities per node:

- **Candidate answer** (path *turns* through this node): `root.val + left_gain + right_gain` — compared against the running global max.
- **Return value** (path continues *upward* to the parent): `root.val + max(left_gain, right_gain)` — but only one branch can extend, and negative gains are clamped to `0` so a parent never inherits a losing detour.

The running max lives on `self`, initialized to `-inf` at the start of `maxPathSum` — which correctly handles all-negative trees (the best path is a single, very negative node).

| | |
|---|---|
| **Time** | O(n) — each node visited once |
| **Space** | O(h) — recursion stack; O(log n) balanced, O(n) worst-case chain |

**Caveat:** `self.res` instance state is initialized at the top of `maxPathSum`, so repeated calls are safe (unlike a bare "self.res = 0 in `__init__`" style). Still, splitting the helper across methods means the caller must remember to reset — the nested/`nonlocal` version scopes it cleanly. The trailing `# dfs(root)` comment is dead code.

## Optimal Solution — Same, polished

Identical algorithm — this is the standard interview solution — with the accumulator scoped to the call via `nonlocal best` and the two roles (turn vs. upward extension) commented at the return sites.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(h) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS with gain + running max (optimal) | **O(n)** | **O(h)** | **Default answer** |
| BFS/iterative post-order | O(n) | O(h)–O(n) | Same logic, more machinery; only needed to dodge recursion limits |
| Recompute best path per node from scratch | O(n²) | O(h) | Never — recomputes subtrees |

**Interview answer:** “Post-order DFS: each node returns its best *upward* gain — `val + max(left_gain, right_gain)`, clamped at 0 — while recording the *turn* value `val + left + right` against a global max. O(n) time, O(h) space; the −inf seed handles all-negative trees.”

## Edge Cases

- **All-negative tree** (`[-2,-1]`) → the single best node (`-1`), not 0 — the `max(0, ...)` clamp only limits what parents inherit, never the answer itself.
- **Single node** → that node's value.
- **Best path is a "turn" at a deep node**, bypassing the root (`[-10,9,20,...,15,7]` → 42 through 20).
- **One-sided path** (root + left chain) → turn never needed; upward gains accumulate.
- **Skewed chain** → O(n) recursion stack; flag for huge inputs.
- **Zig-zag best path** (child's child extends one side only) → return-value rule `max(left, right)` enforces "no revisiting."