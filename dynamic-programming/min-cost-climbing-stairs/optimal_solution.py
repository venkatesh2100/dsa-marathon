from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] = minimum cost to reach step i (i from 0 to len(cost))
        # dp[0] = 0, dp[1] = 0
        # for i >= 2: dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        # answer = dp[len(cost)]
        n = len(cost)
        a, b = 0, 0  # dp[i-2], dp[i-1]
        for i in range(2, n + 1):
            cur = min(a + cost[i-2], b + cost[i-1])
            a, b = b, cur
        return b
