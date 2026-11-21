from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0]

        curr = 1 
        currM = 1
        for num in nums:
            tmp1 = curr * num
            tmp2 = currM * num
            curr = max(tmp1 , tmp2 ,num)
            currM = min(tmp1 , tmp2 ,num)

            res = max(res , curr)

        return res
