from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        sub = []

        def dfs(idx , total):

            if total == target: 
                res.append(sub[:])
                return 

    
            if idx >= len(candidates) or total > target:
                return 

            sub.append(candidates[idx])


            dfs(idx + 1 , total + candidates[idx] )

            sub.pop()
            while idx +1 < len(candidates) and candidates[idx] == candidates[idx+1]:
                idx+=1

            dfs(idx + 1 , total)
        dfs(0, 0)
        return res