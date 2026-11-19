# House Robber II

**Problem:** Houses are arranged in a circle, so house 0 and house n-1 are adjacent — you cannot rob both. Given an integer array `nums` of money at each house, return the maximum amount you can rob without alerting the police (no two adjacent houses, including the circular wrap-around).

**Links:** [NeetCode](https://neetcode.io/problems/house-robber-ii) · [LeetCode 213](https://leetcode.com/problems/house-robber-ii/)

---

## My Solution — DFS + memoization on two linear subarrays

Because the first and last houses are adjacent, you can never rob both. So run the House Robber I recursion on two linear cases:

- `nums[:-1]` — exclude the last house (house 0 may be robbed).
- `nums[1:]` — exclude the first house (house n-1 may be robbed).

Each recursion explores `skip house i` vs `rob house i` with memoization (`dp[i]`). Return `max` of the two results. Special-case `n == 1` (only one house, just rob it).

| | |
|---|---|
| **Time** | O(n) — each of the two linear subarrays is computed once per index |
| **Space** | O(n) — memo arrays plus recursion stack |

**Caveat:** Recursion depth can reach `n`, so large inputs may exceed Python's default recursion limit. Also creates two memo arrays and slices, adding constant-factor overhead.

## Optimal Solution — Iterative DP with O(1) space on two subarrays

Same idea as my solution but iterative: `_rob_linear` computes House Robber I in O(n) time / O(1) space with two rolling variables (`prev = dp[i-2]`, `curr = dp[i-1]`). Call it on `nums[:-1]` and `nums[1:]`, return the max.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + memoization | O(n) | O(n) | Easy to reason about; fine first answer |
| Iterative DP (two vars) | **O(n)** | **O(1)** | **Default interview answer** — same time, no recursion depth risk |

**Interview answer:** "Since houses form a circle, house 0 and n-1 can't both be robbed. So I solve House Robber I on `nums[:-1]` and `nums[1:]`, take the max. House Robber I is `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` computable with two rolling variables in O(n) time / O(1) space. Handle `n == 1` separately."

## Edge Cases

- **`n == 1`** → return `nums[0]` (only one house).
- **`n == 2`** → return `max(nums[0], nums[1])`.
- **All equal values** → rob every other house, respecting the circular constraint.
- **Large input** → iterative version handles it safely; recursive version may need `sys.setrecursionlimit`.