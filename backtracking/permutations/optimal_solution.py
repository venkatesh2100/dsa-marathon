from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        used = [False] * len(nums)

        # At each depth, try every *unused* element in the next position.
        def dfs():
            if len(sub) == len(nums):
                res.append(sub[:])  # copy — `sub` is shared and keeps mutating
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                sub.append(nums[i])
                used[i] = True
                dfs()
                sub.pop()
                used[i] = False

        dfs()
        return res
