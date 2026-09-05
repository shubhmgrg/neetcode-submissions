class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]

        data = {}


        for i in nums:
            data[i] = data.get(i, 0) + 1

        for num, count in data.items():
            freq[count].append(num)

        l = k - 1
        i = len(nums)
        res = []


        while l >= 0 and i >= 0:
            for j in freq[i]:
                if l >= 0:
                    res.append(j)
                    l -= 1
            i -= 1
        
        return res