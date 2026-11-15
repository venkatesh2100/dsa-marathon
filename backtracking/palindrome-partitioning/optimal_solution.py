from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        # is_pal[i][j] = True iff s[i..j] is a palindrome, built bottom-up so
        # the inner check reads already-computed shorter spans.
        is_pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True

        res, part = [], []

        def dfs(i: int):
            if i == n:
                res.append(part[:])
                return
            for j in range(i, n):
                if is_pal[i][j]:  # O(1) instead of an O(n) scan per cut
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res
