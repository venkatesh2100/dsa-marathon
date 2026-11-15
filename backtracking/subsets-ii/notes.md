# Subsets II

**Problem:** Given an integer array that **may contain duplicates**, return all possible subsets (the power set) with no duplicate subsets in the answer.

**Links:** [NeetCode](https://neetcode.io/problems/subsets-ii) · [LeetCode 90](https://leetcode.com/problems/subsets-ii/)

---

## My Solution — Sort + include/exclude with duplicate-run skipping

Sort so identical elements sit adjacent. Same include/exclude recursion as Subsets, with one addition: the **exclude** branch walks `idx` past the entire run of equal candidates before recursing. Skipping "the 2nd copy without the 1st" is exactly the duplicate-generation source — that branch would produce a subset already made by taking the 1st copy.

| | |
|---|---|
| **Time** | O(n · 2ⁿ) worst case — the shape of the answer; dedup keeps the real count at ∏(countᵢ + 1) |
| **Space** | O(n) auxiliary — buffer + recursion depth; output adds O(n · 2ⁿ) |

**Caveat:** `nums.sort()` mutates the caller's list (the optimal takes a sorted copy). The dedup `while` must run **only** on the exclude path — hoisting it before the include branch would break the recursion by advancing `idx` past elements the include branch still needs.

## Optimal Solution — For-loop backtracking with sibling skip

The canonical Subsets II form: record `sub[:]` at **every** tree node (each node is a subset), loop `i` from `start`, and skip a candidate equal to its predecessor *at the same decision level* (`i > start and nums[i] == nums[i-1]`).

| | |
|---|---|
| **Time** | O(n · 2ⁿ) worst case |
| **Space** | O(n) auxiliary + output |

The sibling-skip and the duplicate-run skip are the same idea in two shapes: both prevent "take a later copy without an earlier one."

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| For-loop + sibling skip (optimal) | O(n · 2ⁿ) | O(n) | **Default answer** — record-at-every-node is less code than leaf-only include/exclude |
| Include/exclude + duplicate-run `while` | O(n · 2ⁿ) | O(n) | Equivalent; matches the Combination Sum II shape |
| Generate all subsets → set-dedup | O(n · 2ⁿ) hashing | O(n · 2ⁿ) | Never — dedups after generating instead of while generating |

**Interview answer:** “Sort, backtrack with a for-loop, record every node, and skip equal siblings (`i > start` guard) — dedup is baked into generation. O(2ⁿ) shape, O(n) depth.”

## Edge Cases

- **All identical** (`[4,4,4,4]`) → n + 1 = 5 subsets (`[]` through four 4s) — the dedup at its purest.
- **No duplicates** → behaves exactly like Subsets, 2ⁿ subsets.
- **Two distinct values × duplicates** (`[1,1,2,2]`) → 3 × 3 = 9 subsets (counts of each value independently).
- **Single element** → `[[x], []]`.
- **Empty input** → `[[]]`.
- **Negative values** → fine; sorting handles them.
- **Input mutation** → my version sorts in place; optimal copies first.