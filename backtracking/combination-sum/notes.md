# Combination Sum

**Problem:** Given distinct candidate integers and a target, return all *unique* combinations that sum to the target, where a candidate may be reused unlimited times. Two combinations are duplicates only if they differ in multiset, not order.

**Links:** [NeetCode](https://neetcode.io/problems/combination-target-sum) · [LeetCode 39](https://leetcode.com/problems/combination-sum/)

---

## My Solution — Sort + forward-only backtracking with pruning

Backtrack over a *for loop* starting at `idx` rather than a plain include/exclude branch: pick `nums[i]`, recurse with the **same `i`** (reuse allowed), pop, and continue with `i+1` onward. Because the loop only moves forward, every generated combination is canonical (non-decreasing) — no permutation duplicates. Sorting first turns the "too big" check into a `break`: once `total + nums[i] > target`, every later candidate is too.

| | |
|---|---|
| **Time** | O(n^(T/M)) worst case — branching factor n, depth bounded by T/M (M = smallest candidate); output cost dominates in practice |
| **Space** | O(T/M) recursion depth (M = min candidate) + output |

**Caveat:** `nums.sort()` mutates the caller's list — harmless for the judge, but a side effect worth a comment in review. Without the sort the prune degrades to `continue` and loses the early break. The `total == target` leaf returns immediately, so no wasted work past the target.

## Optimal Solution — Same, polished

Identical algorithm; the only change is `nums = sorted(nums)` — a copy, so the caller's list survives — plus comments on the two invariants (reuse via same `i`; forward-only ⇒ unique multisets).

| | |
|---|---|
| **Time** | O(n^(T/M)) worst case |
| **Space** | O(T/M) depth + output |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Sorted forward backtracking (optimal) | O(n^(T/M)) | O(T/M) | **Default answer** — reuse + uniqueness + prune in ~15 lines |
| Unsorted with `continue` prune | O(n^(T/M)) | O(T/M) | Same bound, slower in practice (no early break) |
| DP count-all-combos | O(n · T) | O(T) | Only when you need the *count* or DP-style reconstruction, not all lists |

**Interview answer:** “Sort, then backtrack with a for-loop from `idx`, recursing on the same `i` for reuse; `break` as soon as a candidate overflows since the array is sorted. Unique multisets fall out of forward-only order.”

## Edge Cases

- **No combination exists** → `[]` (every branch overflows).
- **Single candidate == target** → `[[target]]`.
- **Candidate must repeat** (`[2]`, target 8) → `[[2,2,2,2]]` — the same-`i` recursion.
- **All candidates > target** → `[]` immediately (break at the first loop step).
- **target == 0** → `[[]]` (empty sum; unreachable under LC's `target >= 1` but defensible).
- **Unsorted input** → handled by the sort; note the input mutation (my version) vs copy (optimal).
- **Large target, small min candidate** → depth T/M; the prune keeps fan-out sane.