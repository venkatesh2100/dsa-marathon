from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curr_max, curr_min = 1, 1
        for num in nums:
            if num == 0:
                curr_max, curr_min = 1, 1
                continue
            candidates = (num, curr_max * num, curr_min * num)
            curr_max = max(candidates)
            curr_min = min(candidates)
            res = max(res, curr_max)
        return res
