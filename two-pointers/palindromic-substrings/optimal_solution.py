class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l: int, r: int) -> int:
            cnt = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt

        count = 0
        for i in range(len(s)):
            count += expand(i, i)      # odd length
            count += expand(i, i + 1)  # even length

        return count
