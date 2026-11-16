from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        dic = [(0,1) , (1,0) , (-1,0) , (0,-1)]
        row = len(grid)
        col = len(grid[0])
        res = 0 

        def dfs( r, c):
            nonlocal val
            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == 0: return 
            grid[r][c] = 0
            val+=1
            for dr , dc in dic:
                dfs(dr + r, dc + c)





        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    val = 0
                    dfs(i ,j)
                    res = max(res , val)

        return res 
