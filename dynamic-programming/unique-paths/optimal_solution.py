from math import comb

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # A path needs (m - 1) downs and (n - 1) rights in any order:
        # total (m + n - 2) moves, choose which (m - 1) are downs.
        return comb(m + n - 2, m - 1)
