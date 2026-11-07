from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # One pass: the cheapest price seen so far is the best possible buy;
        # selling today scores price - cheapest. After the min-update,
        # price >= cheapest, so the difference is never negative — no abs needed.
        cheapest, profit = float("inf"), 0
        for price in prices:
            cheapest = min(cheapest, price)
            profit = max(profit, price - cheapest)
        return profit