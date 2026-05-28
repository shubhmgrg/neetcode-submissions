class Solution:
    def numDecodings(self, s: str) -> int:
        
        memo = [0] * len(s)

        def decode(i):

            if i >= len(s):
                return 1

            if s[i] == '0':
                return 0
            
            if i == len(s) - 1:
                return 1
            
            memo[i] = decode(i + 1)

            if s[i] == '1' or (s[i] == '2' and s[i+1] < '7'):
                memo[i] += decode(i+2)
            
            return memo[i]

        return decode(0)