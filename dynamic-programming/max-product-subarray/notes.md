# Maximum Product Subarray

**Problem:** Given an integer array `nums`, find a subarray that has the largest product, and return the product.

**Links:** [NeetCode](https://neetcode.io/problems/maximum-product-subarray) · [LeetCode 152](https://leetcode.com/problems/maximum-product-subarray/)

---

## My Solution — Track Running Max and Min

Keeps `curr` (max product ending here) and `currM` (min product ending here). A negative number swaps which is max and min, so both are recomputed from `curr * num`, `currM * num`, and `num` each step, and `res` tracks the best seen. Zeros naturally reset both to 0, effectively restarting the subarray.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Caveat:** Variable names `curr` / `currM` are terse; the logic is correct but relies on both values being recomputed from the previous step's pair before either is overwritten (the `tmp1` / `tmp2` copies handle this).

## Optimal Solution — Track Running Max & Min with Zero Reset

Same idea, but resets `curr_max` / `curr_min` to `1` on a zero so the subarray restarts cleanly instead of carrying zeros forward. Recomputes both from `(num, curr_max * num, curr_min * num)` each step because a negative flips which is larger.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

This is the standard optimal interview answer. O(n) time is a lower bound since every element may affect the product, and O(1) extra space is best possible.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Running max & min | **O(n)** | **O(1)** | **Default interview answer** |
| Brute force (all subarrays) | O(n²) | O(1) | Never — too slow |
| Division-based prefix products | O(n) | O(1) | Breaks on zeros; avoid |

**Interview answer:** "Track both the max and min product ending at each index, because a negative number flips them. Update both from the previous pair, reset on zero, and keep a running global max. O(n) time, O(1) space."

## Edge Cases

- **Single element** (`[5]`) → `5`
- **All positive** (`[2, 3, 4]`) → product of whole array
- **Contains zero** (`[2, 0, 3]`) → `3` (zero splits subarrays)
- **All negative** (`[-2, -3, -4]`) → `12` (even count of negatives)
- **Odd count of negatives** (`[-2, -3, -1]`) → `6`
- **Negative flips max/min** (`[2, 3, -2, 4]`) → `6`
