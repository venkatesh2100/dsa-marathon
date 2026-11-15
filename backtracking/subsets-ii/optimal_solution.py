from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)  # copy: duplicates must be adjacent, input untouched
        res = []
        sub = []

        # Every node of the decision tree (not just leaves) is a valid subset.
        def dfs(start: int):
            res.append(sub[:])
            for i in range(start, len(nums)):
                # Skip duplicate siblings at the same decision level: taking
                # the 2nd, 3rd, ... copy *without* the 1st yields a subset
                # already generated when the 1st copy was taken.
                if i > start and nums[i] == nums[i - 1]:
                    continue
                sub.append(nums[i])
                dfs(i + 1)
                sub.pop()

        dfs(0)
        return res
