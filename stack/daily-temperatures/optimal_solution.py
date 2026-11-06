from typing import List


class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        res = [0] * n
        stack = []  # indices with temperatures not yet resolved

        for i, t in enumerate(temp):
            while stack and temp[stack[-1]] < t:
                prev = stack.pop()
                res[prev] = i - prev
            stack.append(i)

        return res
