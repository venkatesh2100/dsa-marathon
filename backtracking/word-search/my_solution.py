from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        dic = [(0,1) , (1,0) ,(-1,0) ,(0,-1)]
        vis = set()
        def dfs( r, c , idx):

            if idx == len(word): return True 


            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False 

            if board[r][c] != word[idx]:
                return False 

            if (r ,c ) in vis:
                return False

            vis.add((r,c))
            for dr ,dc in dic:
                if dfs(r + dr , c + dc , idx+1): return True 

            vis.remove((r,c))







        

        for i in range(len(board)):
            for j in range(len(board[0])):

                if board[i][j] == word[0]:
                    if dfs(i ,j , 0):
                        return True 

        return False