# Subtree of Another Tree

**Problem:** Given the roots of two binary trees `root` and `subRoot`, return `True` if `subRoot` is a subtree of `root` — i.e., `root` contains a node whose *entire* subtree (structure and values) is identical to `subRoot`.

**Links:** [NeetCode](https://neetcode.io/problems/subtree-of-a-binary-tree) · [LeetCode 572](https://leetcode.com/problems/subtree-of-another-tree/)

---

## My Solution — DFS + Same-Tree check at every node

Compose two recursions: at each node of `root`, run the Same-Tree (LC 100) comparison against `subRoot`; if it doesn't match, recurse into `root.left` / `root.right` and try again. The `sameTree` helper is the exact 3-line pattern from the previous problem.

| | |
|---|---|
| **Time** | O(n · m) worst case — at each of the n nodes a sameTree comparison of cost O(m) can run (e.g., many equal-valued nodes that keep *almost* matching) |
| **Space** | O(n + m) worst-case stack — isSubtree descends root (≤ n frames) while a failed sameTree holds up to m more |

**Caveat:** The `if not subRoot: return True` branch is dead code under LC's constraint (`1 <= subRoot nodes`); it's a defensible convention but costs a branch. The real cost is redundant re-matching: identical prefixes near the root get compared repeatedly at every node.

## Optimal Solution — Same DFS, polished

Identical algorithm (this *is* the standard interview answer), just restructured: `sameTree` becomes a nested `same` helper (no extra method, no state on `self`), and the three-way `or` collapses the flow. Same O(n · m) / O(n + m).

| | |
|---|---|
| **Time** | O(n · m) worst case |
| **Space** | O(n + m) worst-case stack |

### O(n + m) alternative — serialization + substring search

Serialize both trees to strings *including* null markers (e.g., `N` for null, values comma-separated) and test `sub_serial in root_serial`. With KMP this is provably O(n + m); with CPython's `str.find` it's O(n + m) in practice. The null markers are load-bearing: without them, `[2]` would be found inside `[12]`.

| | |
|---|---|
| **Time** | O(n + m) with KMP |
| **Space** | O(n + m) for the serializations |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + same-tree check | O(n · m) | O(n + m) stack | **Default interview answer** — simple to write and explain |
| Serialize + KMP / `in` | **O(n + m)** | O(n + m) | Follow-up: "can you do better than O(n · m)?" |

**Interview answer:** “At every node of root, run a Same-Tree comparison against subRoot, recursing left/right on failure — O(n·m) worst case. If asked for faster: serialize both trees with null markers and substring-search — O(n + m).”

## Edge Cases

- **Both empty** → `True` (empty is a subtree of empty; per LC constraints subRoot is never empty).
- **subRoot empty, root not** → `True` by the early return.
- **subRoot larger than root** → `False` (every sameTree fails on shape).
- **subRoot == root exactly** → `True` (match at the root).
- **Match buried deep** → found by the left/right recursion.
- **Same values, subRoot has one extra child** (`[4,1,2]` inside `[3,4,5,1,2,×,×,×,×,6]`) → `False` — the classic shape trap; null markers / the two-`None` rule is what catches it.
- **Values that are prefixes of each other** (`2` vs `12`) → only safe because comparisons are per-node values, not string concatenation.