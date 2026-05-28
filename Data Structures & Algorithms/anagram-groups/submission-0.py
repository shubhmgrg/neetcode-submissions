class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anadict = {}
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            if(tuple(count) not in anadict):
                anadict[tuple(count)] = []
            anadict[tuple(count)].append(s)
        
        return list(anadict.values())