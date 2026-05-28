class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1] * len(text1) for _ in range(len(text2))]

        def opt(i, j):
            if i >= len(text2):
                return 0
            if j >= len(text1):
                return 0

            if memo[i][j] != -1:
                return memo[i][j]
            
            if text2[i] == text1[j]:
                memo[i][j] = 1 + opt(i + 1, j + 1)
            else:
                memo[i][j] = max(opt(i, j + 1), opt(i + 1, j))
            
            return memo[i][j]
        
        return opt(0, 0)