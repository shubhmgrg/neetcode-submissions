class Solution:
    def climbStairs(self, n: int) -> int:
        cache = [-1] * n

        def dfs(i):
            if i == 1:
                return 1
            if i == 0:
                return 0
            if i == 2:
                return 2
            if cache[i - 1] != -1:
                return cache[i - 1]
            
            return dfs(i - 2) + dfs(i - 1)
        
        return dfs(n)