class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        res = []

        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                if nums[l] + nums[r] < target:
                    l += 1
                    continue
                if nums[l] + nums[r] > target:
                    r -= 1
                    continue
        
        return res




