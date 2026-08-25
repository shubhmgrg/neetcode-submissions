class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = [0] * 26
        for i in s:
            letters[ord(i) - ord('a')] += 1
        
        for i in t:
            letters[ord(i) - ord('a')] -= 1
        
        final = [0] * 26
        if letters == final:
            return True
        return False