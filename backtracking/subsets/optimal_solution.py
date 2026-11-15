from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        # At each index: include nums[idx], then exclude it.
        def dfs(idx):
            if idx == len(nums):
                res.append(sub[:])  # copy — `sub` keeps mutating after this
                return

            sub.append(nums[idx])
            dfs(idx + 1)
            sub.pop()
            dfs(idx + 1)

        dfs(0)
        return res
