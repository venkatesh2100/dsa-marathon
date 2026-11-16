from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if not fresh:
            return 0

        minutes = 0
        while q and fresh:  # stop the moment the last orange rots
            minutes += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        # rot on enqueue — only fresh (== 1) cells can rot, so the grid marks itself
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

        return minutes if fresh == 0 else -1
