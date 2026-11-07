from typing import List


class Solution:

  def minEatingSpeed(self, piles: List[int], target: int) -> int:
    l = 1
    r = max(piles)

    def check(rate: int) -> int:
      h = 0
      for p in piles:
        # Equivalent to math.ceil(p / rate)
        h += (p + rate - 1) // rate
      return h

    while l < r:
      rate = l + (r - l) // 2

      if check(rate) <= target:
        # Valid speed, but check if a smaller speed also works
        r = rate
      else:
        # Too slow, need a higher speed
        l = rate + 1

    return l
