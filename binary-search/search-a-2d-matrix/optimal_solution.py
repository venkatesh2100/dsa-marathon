from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1

        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]  # map flat index -> (row, col)

            if val == target:
                return True
            # mid is always in [0, m*n - 1] here, so no bounds check is needed
            if val > target:
                r = mid - 1
            else:
                l = mid + 1

        return False
