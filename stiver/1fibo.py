memo = {}
# TOP DOWN 
def fib(n):
    
    if n <=1: return n
    
    if n in memo:
        return memo[n]
    
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]
# print(fib(5))
    
# Bottom Up approach  
def fibBottom(n):
    
    prev , curr = 0 , 1
    
    if n <=1: return n 
    
    for i in range(2, n+1):
        print(prev , curr)
        prev , curr = curr , curr + prev  
        
    return curr 

print(fibBottom(5))