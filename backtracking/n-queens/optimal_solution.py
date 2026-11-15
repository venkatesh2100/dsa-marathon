from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        cols = set()   # occupied columns
        diag1 = set()  # anti-diagonals, keyed by r + c
        diag2 = set()  # main diagonals, keyed by r - c
        res = []

        # Placing row by row means two queens can never share a row by
        # construction -- no row set needed.
        def place(row: int):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if col in cols or (row + col) in diag1 or (row - col) in diag2:
                    continue
                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row + col)
                diag2.add(row - col)

                place(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row + col)
                diag2.remove(row - col)

        place(0)
        return res
