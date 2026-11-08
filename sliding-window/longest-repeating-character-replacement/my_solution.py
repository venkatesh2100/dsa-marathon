class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hmap = {}

        l = 0
        res = 0
        max_freq = 0

        for r in range(len(s)):
            hmap[s[r]] = hmap.get(s[r], 0) + 1

            max_freq = max(max_freq , hmap[s[r]])
            rep = (r - l + 1) - max_freq
            if rep > k:
                hmap[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
            # print(rep , res)

        return res
