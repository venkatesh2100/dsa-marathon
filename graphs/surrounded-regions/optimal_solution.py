from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row, col = len(board), len(board[0])
        dirs = ((0, 1), (1, 0), (-1, 0), (0, -1))

        # Seed every border "O" and stamp it with a "#" sentinel: everything
        # the BFS reaches is border-connected and safe from capture.
        que = deque()
        for r in range(row):
            for c in range(col):
                if (r == 0 or r == row - 1 or c == 0 or c == col - 1) and board[r][c] == "O":
                    board[r][c] = "#"
                    que.append((r, c))

        while que:
            r, c = que.popleft()
            for dr, dc in dirs:
                dx, dy = r + dr, c + dc
                if 0 <= dx < row and 0 <= dy < col and board[dx][dy] == "O":
                    board[dx][dy] = "#"  # mark at enqueue -> each cell queued once
                    que.append((dx, dy))

        # Leftover "O"s never touched the border -> captured;
        # "#" cells were border-connected -> restore them.
        for r in range(row):
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "#":
                    board[r][c] = "O"
