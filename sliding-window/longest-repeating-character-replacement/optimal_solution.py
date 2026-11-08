class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            # Window is uniform iff its "others" count (size - max_freq) fits in k.
            # On violation slide the left edge by EXACTLY ONE -- never a while-loop,
            # so the window size never decreases and the biggest size ever held
            # is always captured in res.
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
