class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        opt = {}

        def change(money):
            if money == 0:
                return 0
            if money in opt:
                return opt[money]


            res = 1e9
            for coin in coins:
                if money - coin >= 0:
                    res = min(res, 1 + change(money - coin))
            
            opt[money] = res
            return res
        
        result = change(amount)

        if result >= 1e9: return -1
        else: return result