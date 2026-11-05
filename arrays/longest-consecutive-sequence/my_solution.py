from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        res = 0
        s = set(nums)


        for val in s:
            if val + 1 not in s:
                c = 1
                while val - 1 in s:
                    c+=1
                    val-=1
                res = max(res , c)

        return res
