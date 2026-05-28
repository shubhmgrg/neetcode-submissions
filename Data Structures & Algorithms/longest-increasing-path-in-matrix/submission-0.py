class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}

        def opt(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            res = 1
            if i + 1 < len(matrix) and matrix[i + 1][j] > matrix[i][j]:
                res = max(res, 1 + opt(i + 1, j))

            if j + 1 < len(matrix[0]) and matrix[i][j + 1] > matrix[i][j]:
                res = max(res, 1 + opt(i, j + 1))
            
            if i - 1 >= 0 and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + opt(i - 1, j))
            
            if j - 1 >= 0 and matrix[i][j - 1] > matrix[i][j]:
                res = max(res, 1 + opt(i, j - 1))
            
            memo[(i, j)] = res

            return res
        
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                result = max(result, opt(i, j))

        return result




        