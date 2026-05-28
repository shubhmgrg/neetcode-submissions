class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        opt = [None] * len(s)

        def canBreak(n):

            if n >= len(s):
                return True
            if opt[n] != None:
                return opt[n]

            for i in range(n, len(s) + 1):
                print(s[n:i])
                if s[n:i] in wordDict and canBreak(i):
                    opt[n] = True
                    return True
    
            opt[n] = False
            return False

        return canBreak(0)