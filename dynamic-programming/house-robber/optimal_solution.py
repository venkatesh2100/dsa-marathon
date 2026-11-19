from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Bottom-up DP with two rolling variables.
        # prev = dp[i-2], curr = dp[i-1]
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr
