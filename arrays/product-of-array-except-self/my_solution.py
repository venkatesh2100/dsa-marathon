from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []

        pre = [1]  * (n + 1)
        suf = [1] *  (n + 1)

        for i in range(1,n+1):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(n-1 , -1,-1):
            suf[i] = suf[i+1] * nums[i]

        # print(pre , suf)
        for i in range(n):
            res.append(pre[i] * suf[i+1])
        return res
