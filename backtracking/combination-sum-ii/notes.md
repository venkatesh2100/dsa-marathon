# Combination Sum II

**Problem:** Given a collection of candidate integers that **may contain duplicates**, and a target, return all unique combinations summing to the target. Each candidate may be used **at most once**; combinations that differ only by which duplicate supplied a value count as the same.

**Links:** [NeetCode](https://neetcode.io/problems/combination-target-sum-ii) · [LeetCode 40](https://leetcode.com/problems/combination-sum-ii/)

---

## My Solution — Sort + include/exclude with duplicate-run skipping

Sort, then at each index branch **include** (recurse `idx+1` with the value added — each element used once) or **exclude** — and the exclude branch first walks `idx` past the entire run of equal candidates, so "skip this 1" also skips its identical siblings. That single `while` is the dedup: the branching "exclude first 1, take second 1" path would produce the same multiset as taking the first, so it's never generated.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) worst case — each element included or excluded; dedup + the `total > target` bail cut real work well below that |
| **Space** | O(n) recursion depth + output |

**Caveat:** `candidates.sort()` mutates the caller's list (harmless for the judge; the optimal takes a sorted copy). The dedup lives in a `while` *after* the include branch — correct, but easy to misplace: it must only advance `idx` for the **exclude** path, never before the include.

## Optimal Solution — For-loop backtracking with sibling-skip + break

The canonical form of the same idea: iterate `i` from `start`; skip a candidate when it equals its predecessor **at the same decision level** (`i > start and nums[i] == nums[i-1]`); and since the array is sorted, `break` the moment `total + nums[i] > target`.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) worst case, with earlier pruning in practice |
| **Space** | O(n) depth + output |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| For-loop + sibling skip + break (optimal) | O(n · 2ⁿ) | O(n) | **Default answer** — one template covers Subsets II / Combination Sum / Permutations II |
| Include/exclude + duplicate-run `while` | O(n · 2ⁿ) | O(n) | Equivalent result; slightly more branch-local logic |
| Set-dedup the naive 2ⁿ subsets | O(n · 2ⁿ) · hashing | O(n · 2ⁿ) | Never — dedups after generating instead of while generating |

**Interview answer:** “Sort, backtrack with a for-loop from `start`, skip `nums[i] == nums[i-1]` when `i > start` (same-level siblings), and `break` on overflow — each element used once via `dfs(i + 1, …)`. O(2ⁿ) shape with dedup built into the generation.”

## Edge Cases

- **Duplicates everywhere** (`[1,1,1]`, target 1) → exactly `[[1]]`, not three copies.
- **Duplicate that must both be used** (`[1,1]`, target 2) → `[[1,1]]` — dedup only applies to *siblings*, not to sequential uses.
- **No combination** (`[2]`, target 3) → `[]`.
- **Single element == target** → `[[x]]`.
- **Unsorted input** → sort handles it; note mutation (my version) vs copy (optimal).
- **Overflow mid-run** → `break` (optimal) / `total > target` bail (mine) cuts branches before the leaf.