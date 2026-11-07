from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2  # avoid overflow in other languages

            if nums[mid] == target:
                return mid
            # jump past mid, not by 1: the half-step is what makes it O(log n)
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        return -1
