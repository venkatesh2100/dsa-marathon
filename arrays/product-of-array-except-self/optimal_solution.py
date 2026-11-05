from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # First pass: res[i] = product of everything before i
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Second pass: multiply in the product of everything after i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
