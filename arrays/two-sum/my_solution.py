from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hmap = {}

        for i in range(len(nums)):

            t = target - nums[i]

            # print('target' , t)
            if t in hmap:
                return [hmap[t] ,i]

            hmap[nums[i]] = i

        return [-1,-1]
