class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        latest = {s[0]: 0}
        n = len(s)
        l = 0
        r = 1
        longest = 1

        while r < n:
            if s[r] in latest:
                while s[r] in latest:
                    del latest[s[l]]
                    l += 1
            latest[s[r]] = r
            r += 1
            if r - l > longest:
                longest = r - l
        
        return longest