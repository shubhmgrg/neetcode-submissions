class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + str(len(i)) + "#" + i
        
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        size = 0
        strs = []
        while i < len(s):
            a = i
            while a < len(s) and s[a] != '#':
                a += 1
            print(s[i:a])
            size = int(s[i:a])
            strs.append(s[a + 1:a+size + 1])
            i = a + size + 1
        
        return strs