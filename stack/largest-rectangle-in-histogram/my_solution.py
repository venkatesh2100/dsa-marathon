from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        res = 0
        heights.append(0)
        for k , v in enumerate(heights):


            while stack and heights[stack[-1]] > v:


                idx = stack.pop()
                width = k if not stack else (k - stack[-1] -1)

                res = max(res , heights[idx] * width)



            stack.append(k)
        return res
