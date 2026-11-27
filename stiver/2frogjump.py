


def frogjump(nums):
    memo = {}
    n = len(nums)
    
    def dfs(idx):
        
        if idx == 0:
            return 0
        if idx in memo:
            return memo[idx]
        left = dfs(idx-1) + abs(nums[idx] - nums[idx-1])
        right = dfs(idx-2) + abs(nums[idx] - nums[idx -2])
        memo[idx] = min(left , right)

        return memo[idx] 
    dfs(n)
            
print(frogjump([30  , 10 , 60 , 10 , 60 , 50]))
        