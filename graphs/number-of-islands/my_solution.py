from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dic = [(0,1) , (1,0) , (-1,0) ,(0,-1)]
        count = 0
        row = len(grid)
        col = len(grid[0])
        def dfs( r, c):

            if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0": return

            grid[r][c] = "0"

            for dr , dc in dic:
                dfs(r + dr , c + dc)



        for i in range(row):
            for j in range(col):

                if grid[i][j] == "1":

                    dfs(i , j)

                    count+=1
        return count
