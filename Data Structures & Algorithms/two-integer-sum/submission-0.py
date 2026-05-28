class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numdict = {}

        for i in range(len(nums)):
            if target - nums[i] in numdict:
                return [numdict[target - nums[i]], i]
            numdict[nums[i]] = i

        return []