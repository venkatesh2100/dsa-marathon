from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def dfs (a):

            if a == 0:
                return 0
            if a in dp:
                return dp[a]
            res = float('inf')
            for c in coins:
                if a - c >=0:
                    res = min(res , 1 + dfs(a - c))
                    dp[a] = res
            return res

        mini  = dfs(amount)
        return -1 if mini == float('inf') else mini 
