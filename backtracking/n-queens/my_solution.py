from typing import List

class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:

        #TODO: Define chessboard , Row col diagonal Set()
        chessboard = [['.'] * n for _ in range(n)]
        # HACK: For checking the Diagonals and Rows Queen properties
        colset = set()
        dia1set = set()
        dia2set = set()
        rowset = set()
        res = []
        def backtracking(row:int):
            # HACK: base condition met to Transform into Normal Matrix
            if row == n:
                copy = chessboard[:]
                ans = []
                for c  in copy:
                    ans.append(''.join(c))
                res.append(ans)
                return
            

            for col in range(n):
                if col in colset or row in rowset or (row+col) in dia1set or (row-col) in dia2set:
                    continue
                chessboard[row][col] = 'Q'
                colset.add(col)
                rowset.add(row)
                dia1set.add(row+col)
                dia2set.add(row-col)

                backtracking(row+1)

                chessboard[row][col] = '.'
                colset.remove(col)
                rowset.remove(row)
                dia1set.remove(row+col)
                dia2set.remove(row-col)
        backtracking(0)
        return res