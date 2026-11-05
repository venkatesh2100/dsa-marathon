# Two Sum II — Input Array Is Sorted

**Problem:** Given a **1-indexed**, sorted array `nums` and a `target`, return the 1-indexed indices `[i, j]` of the two numbers that add up to `target`. Exactly one solution exists, and the same element may not be used twice.

**Links:** [NeetCode 167](https://neetcode.io/problems/two-integer-sum-ii) · [LeetCode 167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

---

## My Solution — Two Pointers from Both Ends

Start with one pointer at each end. If the pair sums to `target`, return the indices plus one. If the sum is too large, the only way to shrink it is to move `right` inward; if it is too small, move `left` inward.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Caveat:** This relies on the input being sorted ascending. Returning `[-1, -1]` is defensive only — the problem guarantees exactly one solution, so that line is unreachable on valid input. The `+1` conversion matters: the problem asks for 1-based indices, not Python's 0-based ones.

## Optimal Solution — Two Pointers (Same Idea, Polished)

Identical logic with clearer names and a single comparison chain. Each step eliminates one candidate value, so at most `n` steps are needed.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

```python
while left < right:
    total = nums[left] + nums[right]

    if total == target:
        return [left + 1, right + 1]
    if total < target:
        left += 1
    else:
        right -= 1
```

This is optimal for the sorted-input version: the two-pointer scan is linear, uses no extra memory, and every step permanently discards one end that cannot be part of the answer. The existing `two-sum` hash-map approach is O(n) time but O(n) space and does not use the sorted property.

## Alternative Approaches

- **Two pointers (my solution / optimal):** O(n) time, O(1) space. Best for sorted input.
- **Hash map:** O(n) time, O(n) space. Needed when the input is unsorted; overkill here.
- **Binary search for each complement:** O(n log n) time, O(1) space. Uses sorting but slower than two pointers.
- **Brute force:** O(n²) time, O(1) space. Never — only for comparison.

---

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Two pointers | **O(n)** | **O(1)** | **Default for sorted input** |
| Hash map | O(n) | O(n) | Input is unsorted (the original Two Sum) |
| Binary search per element | O(n log n) | O(1) | If you think in complements; slower here |
| Brute force | O(n²) | O(1) | Never |

**Interview answer:** Because the array is sorted, use two pointers at the ends. If the sum is too large, move the right pointer left; if it is too small, move the left pointer right. Return the positions plus one. O(n) time and O(1) space.

## Edge Cases

- **Two elements** (`[2, 7]`, target `9`) → `[1, 2]`.
- **Negative numbers** (`[-3, -1, 2, 4]`, target `3`) → `[2, 4]` (`-1 + 4`).
- **Zeros** (`[0, 0, 3]`, target `0`) → `[1, 2]`; equal values at distinct indices are allowed.
- **Duplicate values** (`[1, 1, 2]`, target `2`) → `[1, 2]`; the pair uses two different positions.
- **Answer at the ends** (`[1, 2, 3, 4, 10]`, target `11`) → `[1, 5]`.
- **Answer in the middle** (`[1, 2, 3, 4, 5]`, target `8`) → `[3, 5]`.
- **Large values** → Python integers are arbitrary precision; other languages may need 64-bit sums.
- **No solution** → not possible under the problem constraints; the sentinel `[-1, -1]` is only defensive.
