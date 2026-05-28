class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost) + 1)

        def opt(i, costList):
            if i == 0:
                return 0
            if i == 1:
                return 0
            if i == 2:
                return costList[0]
            
            if cache[i] != -1:
                return cache[i]

            return min(opt(i - 1, costList) + costList[i - 1], opt(i - 2, costList) + costList[i - 2])

        return opt(len(cost), cost)