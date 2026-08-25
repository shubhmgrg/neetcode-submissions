class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        abc = set({})
        for i in nums:
            if i in abc:
                return True
            abc.add(i)
        return False
         