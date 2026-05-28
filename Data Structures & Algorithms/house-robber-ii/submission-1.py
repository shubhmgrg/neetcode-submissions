class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        money1 = [-1] * (len(nums) - 1)
        money2 = [-1] * (len(nums) - 1)

        def opt1(i, houses):
            if i >= len(houses):
                return 0
            if money1[i] != -1:
                return money1[i]
            
            money1[i] = max(opt1(i+1, houses), opt1(i+2, houses) + houses[i])

            return money1[i]
        
        def opt2(i, houses):
            if i >= len(houses):
                return 0
            if money2[i] != -1:
                return money2[i]
            
            money2[i] = max(opt2(i+1, houses), opt2(i+2, houses) + houses[i])

            return money2[i]


        # print(nums[:len(nums) - 1][-1])
        
        # return opt2(0, nums[:len(nums) - 1])
        return max(opt1(0, nums[1:]), opt2(0, nums[:len(nums) - 1]))
            