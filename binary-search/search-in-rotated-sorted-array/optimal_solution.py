from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # One-pass binary search: every window has exactly one sorted half,
        # and the sorted half's value range decides where target can live.
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # nums[l] <= nums[mid] (not <): with <= 2 elements mid == l and the
            # one-element "left half" is trivially sorted — equality keeps that true
            if nums[l] <= nums[mid]:
                # Left half [l..mid] is sorted; strict upper end because
                # target == nums[mid] was already handled above
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # target belongs in the sorted left half
                else:
                    l = mid + 1  # only the rotated right half remains
            else:
                # Right half [mid..r] is sorted; inclusive upper end because
                # nums[r] was never equality-tested — target may sit there
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1