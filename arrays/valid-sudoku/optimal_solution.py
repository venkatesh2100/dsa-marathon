from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                bit = 1 << (int(board[r][c]) - 1)
                box = (r // 3) * 3 + c // 3

                if rows[r] & bit or cols[c] & bit or boxes[box] & bit:
                    return False

                rows[r] |= bit
                cols[c] |= bit
                boxes[box] |= bit

        return True
