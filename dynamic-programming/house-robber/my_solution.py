from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:

        dp = [-1] * len(nums)
        def dfs(i):

            if i >= len(nums): return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(dfs(i+1) , nums[i] + dfs(i+2))
            return dp[i]


        return dfs(0) 
