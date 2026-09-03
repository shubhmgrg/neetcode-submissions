class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = {}
        for i in strs:
            temp = [0] * 26
            for j in i:
                l = ord(j) - ord('a')
                temp[l] += 1
            if tuple(temp) not in anags:
                anags[tuple(temp)] = []
            anags[tuple(temp)].append(i)
        
        return list(anags.values())
