from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        cen = [[False] * 9 for _ in range(9)]  # 3x3 sub-boxes

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                val = int(board[i][j]) - 1
                box_idx = (i // 3) * 3 + (j // 3)

                # Check if the number has already been seen in the row, column, or 3x3 box
                if row[i][val] or col[j][val] or cen[box_idx][val]:
                    return False

                # Mark as seen
                row[i][val] = True
                col[j][val] = True
                cen[box_idx][val] = True

        return True
