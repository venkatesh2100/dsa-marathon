from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        best = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != 1:
                    continue

                area = 0
                grid[i][j] = 0
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    area += 1  # each cell enters the queue exactly once (sunk on enqueue)
                    for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                            grid[nr][nc] = 0
                            q.append((nr, nc))

                best = max(best, area)

        return best
