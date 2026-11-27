# Maximum Subarray

**Problem:** Given an integer array `nums`, find the contiguous subarray with the largest sum and return that sum.

**Links:** [NeetCode](https://neetcode.io/problems/maximum-subarray) · [LeetCode 53](https://leetcode.com/problems/maximum-subarray/)

---

## My Solution — Kadane's Algorithm with Reset

Track `curSum`, the best sum of a subarray ending at the current index. If it ever goes negative, reset it to 0 before adding the next number, because a negative prefix can only hurt future sums. `maxSub` records the best sum seen.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

**Caveat:** Resetting to 0 is safe because `maxSub` is seeded with `nums[0]`; for an all-negative array, every candidate is negative and the best single element is still captured.

## Optimal Solution — Kadane's Recurrence

At each index, the best subarray ending here is either the current number alone (start fresh) or the previous best plus the current number (extend). This expresses Kadane's algorithm directly without a separate reset step.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

This is optimal: every element must be inspected at least once, and only two running values are needed.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Kadane's (recurrence) | **O(n)** | **O(1)** | **Default interview answer** |
| Kadane's (reset on negative) | O(n) | O(1) | Equally good; slightly more explicit |
| Divide and conquer | O(n log n) | O(log n) | Only if asked for a non-DP approach |
| Brute force | O(n²) / O(n³) | O(1) | Never — too slow |

**Interview answer:** "Use Kadane's algorithm: the best subarray ending at each index is either the current element or the previous best plus it. Keep a running maximum. O(n) time, O(1) space."

## Edge Cases

- **Single element** (`[1]`) → `1`
- **All negative** (`[-3, -2, -5]`) → `-2` (must pick one element)
- **All positive** (`[2, 3, 4]`) → `9`
- **Zeros** (`[0, -1, 0]`) → `0`
- **Best subarray in the middle** (`[-2, 1, -3, 4, -1, 2, 1, -5, 4]`) → `6` (`[4, -1, 2, 1]`)
- **Entire array is best** (`[5, 4, -1, 7, 8]`) → `23`
