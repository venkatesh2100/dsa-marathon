# Dynamic Programming

| Problem | Best Approach | Time | Space | Notes |
|---|---|---|---|---|
| [Climbing Stairs](climb-stairs/) | Two rolling variables | O(n) | O(1) | Fibonacci recurrence `ways(i) = ways(i-1) + ways(i-2)`; only the last two values are needed, so two variables replace the array |
| [Min Cost Climbing Stairs](min-cost-climbing-stairs/) | Iterative DP, two variables | O(n) | O(1) | `dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])`; start cost 0 at step 0 or step 1 |
| [House Robber](house-robber/) | Iterative DP, two variables | O(n) | O(1) | `dp[i] = max(dp[i-1], dp[i-2] + nums[i])`; can't rob adjacent houses |
| [House Robber II](house-robber-ii/) | Iterative DP, two variables | O(n) | O(1) | Circular: run House Robber I on `nums[:-1]` and `nums[1:]`, take max |
| [Decode Ways](num-decodings/) | Bottom-up DP, two rolling variables | O(n) | O(1) | `dp[i] = dp[i+1] + (dp[i+2] if 10–26)` |
| [Coin Change](coin-change/) | Bottom-up DP over amounts | O(amount · C) | O(amount) | `dp[a] = 1 + min(dp[a - c])` |
| [Maximum Product Subarray](max-product-subarray/) | Track running max & min | O(n) | O(1) | Negative numbers flip max/min |
| [Word Break](word-break/) | Bottom-up DP over prefixes | O(n²) | O(n) | `dp[i]` = s[:i] segmentable |
| [Unique Paths](unique-paths/) | Combinatorics `C(m+n-2, m-1)` | O(min(m, n)) | O(1) | 2D DP grid; `dp[i][j] = dp[i+1][j] + dp[i][j+1]` |