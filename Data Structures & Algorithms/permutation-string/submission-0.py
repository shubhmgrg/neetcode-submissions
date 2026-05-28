class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        dict1 = {}
        dict2 = {}
        a = 'abcdefghijklmnopqrstuvwxyz'

        for i in range(26):
            dict1[a[i]] = 0
            dict2[a[i]] = 0
        
        for i in range(len(s1)):
            dict1[s1[i]] += 1
            dict2[s2[i]] += 1

        if dict1 == dict2:
            return True
        

        i = len(s1)
        while i < len(s2):
            dict2[s2[i - len(s1)]] = max(0, dict2[s2[i - len(s1)]] - 1)
            dict2[s2[i]] += 1
            if dict1 == dict2:
                return True
            i += 1


        return False