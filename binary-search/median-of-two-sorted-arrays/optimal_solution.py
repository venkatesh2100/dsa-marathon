from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Binary search on PARTITION SIZES, not values: choose i elements from
        # nums1 and half - i from nums2 so that every element on the left side
        # is <= every element on the right side. Search space is log(min(m, n)).
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1  # always partition the smaller array
        m, n = len(nums1), len(nums2)
        total = m + n
        # Left partition gets half elements; (total + 1) // 2 puts the odd
        # case's median element on the left side, simplifying the return
        half = (total + 1) // 2

        # Binary search i = left-partition size taken from nums1, in [0, m]
        l, r = 0, m
        while True:
            i = (l + r) // 2
            j = half - i                       # taken from nums2

            # Boundary values on each side of the cut; out-of-range cuts
            # become +/-inf so they can never violate the ordering
            aL = nums1[i - 1] if i > 0 else float("-inf")   # last elem of A-left
            aR = nums1[i] if i < m else float("inf")        # first elem of A-right
            bL = nums2[j - 1] if j > 0 else float("-inf")   # last elem of B-left
            bR = nums2[j] if j < n else float("inf")        # first elem of B-right

            # Right edge: a valid cut keeps aL <= bR and bL <= aR
            if aL <= bR and bL <= aR:
                if total % 2 == 1:
                    return float(max(aL, bL))               # median is the left max
                return (max(aL, bL) + min(aR, bR)) / 2      # mean of seam values
            elif aL > bR:
                r = i - 1  # too many taken from nums1
            else:
                l = i + 1  # too few taken from nums1