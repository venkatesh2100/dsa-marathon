from typing import List


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sorted() copy: same pruning power as in-place sort, but the caller's
        # list is left untouched.
        nums = sorted(nums)
        res = []
        sub = []

        # Reuse allowed -> recurse with i (not i + 1); moving forward only is
        # what keeps each combination unique regardless of order.
        def dfs(idx: int, total: int):
            if total == target:
                res.append(sub[:])
                return
            for i in range(idx, len(nums)):
                if total + nums[i] > target:
                    break  # sorted: everything after nums[i] is too big too
                sub.append(nums[i])
                dfs(i, total + nums[i])
                sub.pop()

        dfs(0, 0)
        return res
