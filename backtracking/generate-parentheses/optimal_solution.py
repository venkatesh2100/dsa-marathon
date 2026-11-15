from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sub = []

        # Invariant: 0 <= c <= o <= n. Two moves: open "(" while o < n,
        # close ")" while c < o. A prefix never has more ")" than "(".
        def dfs(o: int, c: int):
            if o == c == n:
                res.append("".join(sub))
                return
            if o < n:
                sub.append("(")
                dfs(o + 1, c)
                sub.pop()
            if c < o:
                sub.append(")")
                dfs(o, c + 1)
                sub.pop()

        dfs(0, 0)
        return res
