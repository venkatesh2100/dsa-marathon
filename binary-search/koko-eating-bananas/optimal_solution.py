from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search on the answer: smallest feasible rate in [1, max(piles)]
        l, r = 1, max(piles)

        def hours_needed(rate: int) -> int:
            total = 0
            for p in piles:
                total += (p + rate - 1) // rate  # ceil(p / rate), no float error
            return total

        # Lower-bound template: while l < r, mid stays a candidate, so use r = mid
        while l < r:
            mid = (l + r) // 2
            if hours_needed(mid) <= h:
                r = mid      # mid works; something smaller might too
            else:
                l = mid + 1  # mid is too slow
        return l
