from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        row, col = len(grid), len(grid[0])
        count = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] != "1":
                    continue

                count += 1
                grid[i][j] = "0"
                q = deque([(i, j)])
                while q:
                    r, c = q.popleft()
                    for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == "1":
                            grid[nr][nc] = "0"  # sink on enqueue — a cell can never enter the queue twice
                            q.append((nr, nc))

        return count
