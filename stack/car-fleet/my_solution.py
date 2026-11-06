from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:


        # res = [ target - v for v in position]
        pair = sorted(zip(position , speed) , reverse=True)

        stack = []
        # print(pair)
        for p , s in  pair:

            t = (target -  p)/s

            stack.append(t)

            while len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)



        # return len(s)
