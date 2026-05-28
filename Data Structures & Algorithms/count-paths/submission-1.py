class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[-1] * n for _ in range(m)]

        if m == 1 and n == 1:
            return 1

        def opt(a, b):
            if a == (m - 2) and b == (n - 1):
                return 1
            if a == (m - 1) and b == (n - 2):
                return 1

            if grid[a][b] != -1:
                return grid[a][b]
            
            res = 0
            if a < (m - 1):
                res += opt(a + 1, b)
            if b < (n - 1):
                res += opt(a, b + 1)

            grid[a][b] = res
            print(res)
            return res
        
        return opt(0,0)