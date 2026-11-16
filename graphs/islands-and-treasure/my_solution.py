from collections import deque
from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:


        dic = [(0, 1) , (1,0) , (-1,0) , (0,-1)]

        row = len(grid)
        col = len(grid[0])
        que = deque([])
        vis = set()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    que.append((i,j))
                    vis.add((i,j))
        dis = 1
        while que:

            for _ in range(len(que)):
                r , c = que.popleft()
                for dr , dc in dic:

                    dx , dy = dr + r , dc + c
                    if dx < 0 or dx >= row or dy < 0 or dy >= col or grid[dx][dy] == -1 or (dx , dy) in vis:
                        continue

                    grid[dx][dy] = dis
                    que.append((dx,dy))
                    vis.add((dx,dy))
            dis+=1
