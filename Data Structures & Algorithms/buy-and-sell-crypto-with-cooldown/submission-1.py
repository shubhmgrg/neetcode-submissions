class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}

        def opt(i, buying):

            if i >= len(prices):
                return 0
            
            if (i, buying) in memo:
                return memo[(i, buying)]
            
            res = opt(i + 1, buying)
            if buying:
                res = max(opt(i+1, not buying) - prices[i], res)
            else:
                res = max(opt(i + 2, not buying) + prices[i], res)
            
            memo[(i, buying)] = res

            return res
        
        return opt(0, True)
