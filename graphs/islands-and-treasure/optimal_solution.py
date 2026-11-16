from collections import deque
from typing import List

INF = 2147483647


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid or not grid[0]:
            return

        row, col = len(grid), len(grid[0])
        # multi-source BFS: every gate is a seed at distance 0
        q = deque((i, j) for i in range(row) for j in range(col) if grid[i][j] == 0)

        dis = 0  # distance of the cells currently in the queue
        while q:
            dis += 1
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == INF:
                        # only INF cells are fillable, so the grid marks itself — no visited set
                        grid[nr][nc] = dis
                        q.append((nr, nc))
