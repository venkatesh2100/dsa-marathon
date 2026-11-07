from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Binary search for the inflection point: the one index where a value
        # is greater than the one that follows it. Comparing mid against the
        # RIGHT end (not the left) separates the two cases unambiguously.
        l, r = 0, len(nums) - 1

        # Lower-bound template: while l < r, mid stays a candidate, so use r = mid
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1  # drop is strictly right of mid; min can't be at mid
            else:
                r = mid      # [mid..r] is sorted; min is at mid or further left
        return nums[l]
