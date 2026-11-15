# Subsets

**Problem:** Given an array of distinct integers, return *all* possible subsets (the power set) — the answer itself must not contain duplicate subsets.

**Links:** [NeetCode](https://neetcode.io/problems/subsets) · [LeetCode 78](https://leetcode.com/problems/subsets/)

---

## My Solution — Include/exclude backtracking

At each index, the recursion makes a binary choice: **include** `nums[idx]` (append, recurse, pop) or **exclude** it (recurse). At `idx == len(nums)` the current `sub` is a complete subset and is copied into `res`. 2ⁿ leaves = 2ⁿ subsets.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) — 2ⁿ subsets, each copied at a leaf in up to O(n) |
| **Space** | O(n) auxiliary — recursion depth + the shared `sub` buffer; the output adds O(n · 2ⁿ) |

**Caveat:** None algorithmic — this is the canonical optimal. The only trap is copying: `res.append(sub)` (no slice) appends a *reference*, and since `sub` keeps popping, every recorded subset would end up empty. `sub[:]` is load-bearing.

## Optimal Solution — Same, polished

Identical include/exclude recursion — it's already optimal (the output size *is* the lower bound). Polish: comment the copy rule and keep the symmetric append/pop pair adjacent.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) |
| **Space** | O(n) auxiliary + O(n · 2ⁿ) output |

### Alternatives

- **Iterative doubling:** start with `[[]]`; for each number, append `subset + [num]` for every existing subset. O(n · 2ⁿ), no recursion.
- **Bitmask:** for `mask` in `0..2ⁿ−1`, the set bits pick which elements are in. Same complexity; n ≤ ~20 range.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Include/exclude DFS (optimal) | **O(n · 2ⁿ)** | **O(n)** aux | **Default answer** — template generalizes to Subsets II, Permutations, Combination Sum |
| Iterative doubling | O(n · 2ⁿ) | O(n · 2ⁿ) | No-recursion settings; trivially iterates |
| Bitmask enumeration | O(n · 2ⁿ) | O(n) aux | Fun one-liner style; same bound |

**Interview answer:** “At each index, branch include/exclude, copying `sub` at the leaves — O(n · 2ⁿ) time, which is forced since the output has 2ⁿ subsets of size up to n.”

## Edge Cases

- **Empty input** → `[[]]` — the empty set is a subset; the recursion immediately hits the leaf.
- **Single element** → `[[x], []]` (order: include-first).
- **All distinct** (LC guarantee) → exactly 2ⁿ unique subsets; no dedup needed.
- **Subsets II follow-up (duplicates)** → sort + skip equal siblings at the same recursion level; the copy-at-leaf rule is unchanged.
- **Large n** → 2ⁿ explodes past n ≈ 25; flag the combinatorial wall.