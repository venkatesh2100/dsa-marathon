from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []

        sub = []

        def dfs(o , c):

            if o == c == n:
                res.append("".join(sub))

                return 
            
            if o < n:
                sub.append("(")
                dfs(o + 1, c)
                sub.pop()

            if c < o:
                sub.append(")")
                dfs(o , c + 1)
                sub.pop()

        dfs(0 , 0)

        return res