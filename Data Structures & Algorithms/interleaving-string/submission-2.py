class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}

        def opt(i, j):
            if (i,j) in cache:
                return cache[(i, j)]
            if i + j >= len(s3):
                return i >= len(s1) and j >= len(s2)
            if j >= len(s2):
                return s1[i:] == s3[j + i:]
            if i >= len(s1):
                return s2[j:] == s3[j + i:]

            
            if s1[i] == s3[i + j] and s2[j] == s3[i + j]:
                res = opt(i + 1, j) or opt(i, j + 1)
            elif s1[i] == s3[i + j]:
                res = opt(i + 1, j)
            elif s2[j] == s3[i + j]:
                res = opt(i, j + 1)
            else:
                res = False
            
            cache[(i, j)] = res
            return res
        
        return opt(0, 0)

