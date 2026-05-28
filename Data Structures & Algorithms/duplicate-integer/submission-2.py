class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myDict = set([])
        for i in nums:
            if i in myDict:
                return True
            myDict.add(i)
        
        return False