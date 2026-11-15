from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # sorted() copy: non-mutating, and the sort enables both the duplicate
        # skip and the overflow break.
        nums = sorted(candidates)
        res = []
        sub = []

        def dfs(start: int, total: int):
            if total == target:
                res.append(sub[:])
                return
            for i in range(start, len(nums)):
                # Skip duplicate siblings at the same decision level.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                if total + nums[i] > target:
                    break  # sorted: every later candidate is too big too
                sub.append(nums[i])
                dfs(i + 1, total + nums[i])
                sub.pop()

        dfs(0, 0)
        return res
