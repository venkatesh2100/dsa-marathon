from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        dic = [(0,1) , (1,0) , (-1,0) , (0,-1)]

        row , col = len(board) , len(board[0])

        que = deque([])
        vis = set()

        for r in range(row):
            for c in range(col):
                if (r == 0 or c == 0 or r == row - 1 or c == col -1) and  board[r][c] == "O":
                    que.append((r,c))
                    vis.add((r,c))

        while que:

            r ,c = que.popleft()

            for dr , dc in dic:

                dx , dy = r + dr , c + dc

                if dx < 0 or dx >= row or dy < 0 or dy >= col or (dx , dy) in vis:
                    continue

                if board[dx][dy] == "O":
                    que.append((dx,dy))
                    vis.add((dx,dy))


        for r in range(row):
            for c in range(col):
                if board[r][c] == "O" and (r,c) not in vis:
                    board[r][c] = "X"
