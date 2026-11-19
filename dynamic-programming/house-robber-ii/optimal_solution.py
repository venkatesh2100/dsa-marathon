from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Houses are in a circle, so house 0 and house n-1 are adjacent.
        # Can't rob both → run House Robber I on two linear subarrays:
        #   nums[:-1] (exclude last house) and nums[1:] (exclude first house).
        # Take the max of the two.
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self._rob_linear(nums[:-1]), self._rob_linear(nums[1:]))

    def _rob_linear(self, nums: List[int]) -> int:
        # House Robber I, O(1) space: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        prev, curr = 0, 0
        for x in nums:
            prev, curr = curr, max(curr, prev + x)
        return curr
