from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # indices of bars with strictly increasing heights
        res = 0

        for k, v in enumerate(heights + [0]):  # trailing 0 flushes the stack
            while stack and heights[stack[-1]] > v:
                h = heights[stack.pop()]
                # first shorter bar on the right is k, on the left is stack[-1]
                width = k if not stack else k - stack[-1] - 1
                res = max(res, h * width)
            stack.append(k)

        return res
