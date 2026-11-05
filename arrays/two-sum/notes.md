# Two Sum

**Problem:** Given an array `nums` and an integer `target`, return the indices of the two numbers that add up to `target`. Exactly one solution exists, and the same element cannot be used twice.

**Links:** [NeetCode 1](https://neetcode.io/problems/two-integer-sum) · [LeetCode 1](https://leetcode.com/problems/two-sum/)

---

## My Solution — One-Pass Hash Map

For each number, compute its complement (`target - num`) and check whether the complement was already seen. Store `value -> index` as you go. Checking **before** inserting guarantees the same index is never reused.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

**Caveat:** The `[-1, -1]` fallback is unreachable under the problem constraints (exactly one solution is guaranteed). It is harmless but could be `[]`.

## Optimal Solution — Same Idea, Cleaned Up

The one-pass hash map is the optimal approach: every element is visited once and each lookup is O(1) on average. `enumerate` removes the manual indexing.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) |

```python
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

## Alternative Approaches

- **Brute force:** O(n²) time, O(1) space. Compare every pair — only useful to explain why hashing helps.
- **Sort + two pointers:** O(n log n) time, O(n) space. Works when returning values, but here we need original indices, so the indices must be stored and sorted alongside.
- **Two-pass hash map:** O(n) time, O(n) space. Build the full map first, then search — simpler to reason about but does two passes and needs an index check to avoid reusing an element.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| One-pass hash map | **O(n)** | O(n) | **Default answer** — fastest, handles duplicates correctly |
| Two-pass hash map | O(n) | O(n) | Easier to explain, but unnecessary second pass |
| Sort + two pointers | O(n log n) | O(n) | Only when the original indices are not required |
| Brute force | O(n²) | O(1) | Never — only for comparison |

**Interview answer:** Use a hash map from value to index. For each element, check whether `target - num` is already in the map; if it is, return both indices, otherwise store the current element. One pass, O(n) time, O(n) space.

## Edge Cases

- Duplicate values `([3, 3], 6)` → `[0, 1]`. Checking before inserting prevents returning `[0, 0]`.
- Negative numbers `([-1, -2, -3, -4], -6)` → `[1, 3]`.
- Zero target `([-2, 2], 0)` → `[0, 1]`.
- Target not present → fallback (`[-1, -1]` / `[]`); cannot happen under the stated constraints.
- Single element → no valid pair, but constraints guarantee a solution exists.
