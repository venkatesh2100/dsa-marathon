from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = 0
        res = 0
        r = len(heights) - 1

        while l < r:

            if heights[l] < heights[r]:
                l+=1
                res = max(res  , heights[l] * (r - l))
            else:
                res = max( res , heights[r] * (r-1))
                r-=1
            print(res)
        return res
