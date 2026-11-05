from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # Edge case: encode empty list distinctly to avoid colliding with [""]
        if not strs:
            return ""

        ans = ""
        for v in strs:
            for i in range(len(v)):
                ans += str(ord(v[i]))
                ans += "#"
            ans += "-"  # Keep the '-' on all words including the last
        return ans

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        res = []
        l, r = 0, 0
        while r < len(s):
            sub = []
            while r < len(s) and s[r] != "-":
                while r < len(s) and s[r] != "#":
                    r += 1

                sub.append(chr(int(s[l:r])))
                r += 1  # Skip past '#'
                l = r
            res.append("".join(sub))
            r += 1  # Skip past '-'
            l = r

        return res
