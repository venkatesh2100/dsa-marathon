class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l: int, r: int) -> tuple[int, int]:
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            # step back to the last valid palindrome bounds
            return l + 1, r - 1

        best_start, best_end = 0, 0
        for i in range(len(s)):
            l1, r1 = expand(i, i)      # odd length
            l2, r2 = expand(i, i + 1)  # even length
            if r1 - l1 > best_end - best_start:
                best_start, best_end = l1, r1
            if r2 - l2 > best_end - best_start:
                best_start, best_end = l2, r2

        return s[best_start : best_end + 1]
