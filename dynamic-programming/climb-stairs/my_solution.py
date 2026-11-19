class Solution:
    def climbStairs(self, n: int) -> int:
        

        arr = [0 , 1]
        if n == 1 or n == 0:
            return 1
        

        for i in range(2,n+2):
            arr.append(arr[i-1] + arr[i-2])
        # print(arr)
        return arr[n+1] 
