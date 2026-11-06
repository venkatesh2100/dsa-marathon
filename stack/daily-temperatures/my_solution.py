from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:

        stack = []

        res = [0] * len(temp)

        for k , v in enumerate(temp):

            while stack and temp[stack[-1]] < v:

                res[stack[-1]] = k - stack[-1]

                stack.pop() 

            stack.append(k)

        return res
