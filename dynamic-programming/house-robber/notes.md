# House Robber

**Problem:** You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, and adjacent houses have security systems connected — you cannot rob two adjacent houses. Given an integer array `nums` representing the amount of money at each house, return the maximum amount of money you can rob tonight without alerting the police.

**Links:** [NeetCode](https://neetcode.io/problems/house-robber) · [LeetCode 198](https://leetcode.com/problems/house-robber/)

---

## My Solution — DFS with memoization

From each house `i` you either skip it (`dfs(i+1)`) or rob it (`nums[i] + dfs(i+2)`). Memoize results in `dp[i]` so each index is computed at most once. Start at house 0.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(n) — memo array `dp` plus recursion stack |

**Caveat:** Recursion depth reaches `n` in the worst case (skipping every house), so very large inputs can exceed Python's default recursion limit (~1000). An iterative bottom-up approach avoids this.

## Optimal Solution — Iterative DP, O(1) space

The same recurrence `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` can be computed bottom-up while keeping only the two most recent values. `prev = dp[i-2]`, `curr = dp[i-1]`, and for each house `x`: `curr = max(curr, prev + x)`, then shift.

| | |
|---|---|
| **Time** | O(n) |
| **Space** | O(1) |

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| DFS + memoization | O(n) | O(n) | Easy to write recursively; good first answer |
| Iterative DP (two vars) | **O(n)** | **O(1)** | **Default interview answer** — same time, no recursion depth risk |
| Array DP | O(n) | O(n) | Fine if you want a visible table; unnecessary extra space |

**Interview answer:** "This is a classic DP: at each house, choose to skip it or rob it plus the best from two houses back. The recurrence is `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`. I can solve it iteratively with two rolling variables in O(n) time and O(1) space."

## Edge Cases

- **Empty `nums`** → `0` (nothing to rob).
- **Single house** → rob that house: `nums[0]`.
- **Two houses** → rob the richer of the two: `max(nums[0], nums[1])`.
- **All equal values** → rob every other house.
- **Large input** → iterative version handles it safely; recursive version may need `sys.setrecursionlimit`.