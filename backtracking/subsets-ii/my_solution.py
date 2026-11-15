from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # 1. Group identical elements together
        res = []
        sub = []

        def dfs(idx: int):
            if idx == len(nums):
                res.append(sub[:])
                return

            # Choice 1: Include nums[idx]
            sub.append(nums[idx])
            dfs(idx + 1)
            sub.pop()

            # Choice 2: Exclude nums[idx] AND skip all duplicate copies of it
            while idx + 1 < len(nums) and nums[idx] == nums[idx + 1]:
                idx += 1
            dfs(idx + 1)

        dfs(0)
        return res