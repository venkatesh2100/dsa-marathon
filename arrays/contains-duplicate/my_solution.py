from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in range(len(nums)):
            hmap[nums[i]] = hmap.get(nums[i], 0) + 1

            if hmap[nums[i]] > 1:
                return True

        return False
