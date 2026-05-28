class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = [-1] * len(prices)

        def opt(i):
            if i >= len(prices):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            res = opt(i + 1)
            for j in range(i + 1, len(prices)):
                res = max(prices[j] - prices[i] + opt(j + 2), res)
            
            return res
        
        return opt(0)
