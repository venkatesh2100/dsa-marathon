from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l = 0
        m, n = len(matrix), len(matrix[0])
        r = (m * n) - 1

        while l <= r:

            mid = l + (r - l) // 2

            idx1 = mid // n
            idx2 = mid % n
            # print(idx1 , idx2)
            # if 0 > idx1 or 0 > idx2 or idx1 >= m or idx2 >= n: return False
            if matrix[idx1][idx2] == target: return True
            elif matrix[idx1][idx2] > target: r = mid - 1
            else: l = mid + 1

        return False
