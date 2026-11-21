# Unique Paths

**Problem:** A robot is at the top-left corner of an `m x n` grid. It can only move down or right. Return the number of unique paths to the bottom-right corner.

**Links:** [NeetCode](https://neetcode.io/problems/unique-paths) · [LeetCode 62](https://leetcode.com/problems/unique-paths/)

---

## My Solution — 2D DP Table, Bottom-Right to Top-Left

Allocates an `(m + 1) x (n + 1)` table (the extra row/column act as zero boundaries). Seeds `dp[m-1][n-1] = 1` (one way to stand at the destination) and fills backwards: `dp[i][j] += dp[i+1][j] + dp[i][j+1]`, meaning paths from `(i,j)` equal paths going down plus paths going right. Returns `dp[0][0]`.

| | |
|---|---|
| **Time** | O(m · n) |
| **Space** | O(m · n) |

**Caveat:** The table is one row and column larger than needed; only indices `0..m-1` and `0..n-1` are meaningful. The `print(dp)` is left in from the original attempt — remove it for a clean submission.

## Optimal Solution — Combinatorics

Every valid path uses exactly `(m - 1)` down moves and `(n - 1)` right moves, in any order: `(m + n - 2)` total moves, choose which `(m - 1)` are downs. That's `C(m + n - 2, m - 1)`.

| | |
|---|---|
| **Time** | O(min(m, n)) |
| **Space** | O(1) |

This is mathematically optimal — no DP table needed at all. If the interviewer wants to see DP, use the 1D rolling-array version (`dp[j] += dp[j-1]` row by row) which is O(m · n) time and O(n) space.

## Which One to Pick

| Approach | Time | Space | When to use |
|---|---|---|---|
| Combinatorics (`math.comb`) | **O(min(m, n))** | **O(1)** | **Best answer** — closed form |
| 2D DP table | O(m · n) | O(m · n) | Intuitive first attempt |
| 1D rolling DP | O(m · n) | O(n) | When interviewer wants DP with space optimization |

**Interview answer:** "Each path is `(m-1)` downs and `(n-1)` rights in some order, so the answer is `C(m+n-2, m-1)`. If you want to see DP, I can do a 1D rolling array: `dp[j] += dp[j-1]` row by row, O(m·n) time and O(n) space."

## Edge Cases

- **`m = 1` or `n = 1`** → `1` (only one straight path)
- **`m = 1, n = 1`** → `1` (already at destination)
- **Small grid** (`3 x 3`) → `6`
- **Square grid** → symmetric: `uniquePaths(m, n) == uniquePaths(n, m)`
