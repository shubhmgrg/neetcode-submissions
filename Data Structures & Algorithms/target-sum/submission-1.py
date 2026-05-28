class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = {}

        def opt(amount, i):
            if i == len(nums) and amount == 0:
                return 1
            if i >= len(nums):
                return 0
            if (amount, i) in memo:
                return memo[(amount, i)]
            
            res = opt(amount - nums[i], i + 1)
            res += opt(amount + nums[i], i + 1)

            memo[(amount, i)] = res
            return res
        
        return opt(target, 0)