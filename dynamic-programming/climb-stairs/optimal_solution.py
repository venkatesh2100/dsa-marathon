class Solution:
    def climbStairs(self, n: int) -> int:
        # ways(i) = ways(i - 1) + ways(i - 2), seeded with ways(0) = ways(1) = 1.
        # Only the last two values are ever needed, so keep them in two variables.
        prev, curr = 1, 1
        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr
        return curr
