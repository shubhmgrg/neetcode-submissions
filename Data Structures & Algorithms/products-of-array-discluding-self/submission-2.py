class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftSide = [1]
        rightSide = [1]
        left = 1
        right = 1
        size = len(nums)
        for i in range(size - 1):
            left = left * nums[i]
            leftSide.append(left)
            right = right * nums[size - i - 1]
            rightSide.append(right)
        rightSide.reverse()
        res = []
        for i in range(size):
            res.append(leftSide[i] * rightSide[i])
        
        return res