class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        b = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 0
            if t[i] not in b:
                b[t[i]] = 0
            a[s[i]] += 1
            b[t[i]] += 1
        
        return a == b