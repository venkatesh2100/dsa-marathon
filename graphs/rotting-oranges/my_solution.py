from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        dic = [(0,1) ,(1,0) ,(-1,0) ,(0,-1)]
        row , col = len(grid) , len(grid[0])
        res = -1
        count = 0
        que = deque([])
        vis = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    que.append((i,j))
                    vis.add((i,j))
                elif grid[i][j] == 1:
                    count+=1
        if not count: return 0
        while que:

            for _ in range(len(que)):
                r , c = que.popleft()

                for dr , dc in dic:
                    dx  , dy = dr + r , dc + c

                    if dx < 0 or dx >= row or dy < 0 or dy >= col or grid[dx][dy]==0 or (dx , dy) in vis:
                        continue

                    grid[dx][dy] = 2
                    count-=1
                    que.append((dx,dy))
                    vis.add((dx,dy))

            res+=1

        return res if not count else -1
