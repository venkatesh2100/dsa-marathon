from functools import cache

class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dfs(i):
            # Base case: reached the end of the string -> 1 valid way
            if i == len(s):
                return 1
            
            # Invalid: no letter starts with '0'
            if s[i] == '0':
                return 0

            # Choice 1: Take 1 digit (always valid since s[i] != '0')
            ways = dfs(i + 1)

            # Choice 2: Take 2 digits (valid only if two digits exist and form 10..26)
            if i + 1 < len(s) and 10 <= int(s[i : i + 2]) <= 26:
                ways += dfs(i + 2)

            return ways

        return dfs(0)
