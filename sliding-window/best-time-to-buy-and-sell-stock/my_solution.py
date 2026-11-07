from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        res = 0

        for p in prices:
            # print(p,mini)
            buy = min(buy , p)

            res = max(res , abs(p -buy))

        return res