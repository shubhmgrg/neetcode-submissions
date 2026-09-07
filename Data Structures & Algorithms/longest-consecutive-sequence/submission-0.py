class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        big = 0
        length = 0

        new = set(nums)

        for i in new:
            j = i
            if j - 1 not in new:
                length = 1
                while j + 1 in new:
                    length += 1
                    j += 1
                if length > big:
                    big = length

        return big