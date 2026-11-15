from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        res = []

        sub = []
        used = [False] * len(nums)
        def dfs():


            if len(sub) == len(nums):
                res.append(sub[:])

                return 

            
            for i in range(len(nums)):
                if used[i]: continue
                sub.append(nums[i])
                used[i] = True
                dfs()

                sub.pop()
                used[i] = False
        dfs()
        return res