from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dfs(i: int, arr: List[int], dp: List[int]) -> int:
            if i >= len(arr):
                return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(dfs(i + 1, arr, dp), arr[i] + dfs(i + 2, arr, dp))
            return dp[i]

        arr1 = nums[:-1]
        arr2 = nums[1:]

        return max(
            dfs(0, arr1, [-1] * len(arr1)),
            dfs(0, arr2, [-1] * len(arr2))
        ) 
