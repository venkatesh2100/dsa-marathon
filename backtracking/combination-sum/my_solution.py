from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # Smallest values first
        res = []
        sub = []

        def dfs(idx: int, total: int):
            if total == target:
                res.append(sub[:])
                return

            for i in range(idx, len(nums)):
                # Because nums is sorted, if nums[i] is too big,
                # every number after it is also too big -> stop immediately!
                if total + nums[i] > target:
                    break

                sub.append(nums[i])
                dfs(i, total + nums[i])
                sub.pop()

        dfs(0, 0)
        return res