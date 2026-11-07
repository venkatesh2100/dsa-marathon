class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        uq = set()
        res = 0

        l = 0
        r = 0

        while r < len(s):
            if s[r] in uq:
                while s[r] in uq:
                    uq.remove(s[l])
                    l+=1
            uq.add(s[r])
            res = max(res , (r - l) + 1)
            r+=1
        return res