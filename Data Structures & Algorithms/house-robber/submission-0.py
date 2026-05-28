class Solution:
    def rob(self, nums: List[int]) -> int:
        houses = [-1] * len(nums)

        def opt(i):
            if i >= len(nums):
                return 0
            if houses[i] != -1:
                return houses[i]
            
            houses[i] = max(opt(i+1), opt(i+2) + nums[i])

            return houses[i]
        
        return opt(0)