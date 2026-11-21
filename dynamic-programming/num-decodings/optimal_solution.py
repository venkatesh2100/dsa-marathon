class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        # dp[i] = ways to decode s[i:]; only dp[i+1] and dp[i+2] are needed.
        # next_one = dp[i+1], next_two = dp[i+2]; seed dp[n] = 1, dp[n+1] = 0.
        next_one, next_two = 1, 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = next_one
                if i + 1 < n and 10 <= int(s[i : i + 2]) <= 26:
                    cur += next_two
            next_two, next_one = next_one, cur
        return next_one
