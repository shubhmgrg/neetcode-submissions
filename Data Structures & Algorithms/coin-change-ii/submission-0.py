class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        memo = {}

        def opt(i, a):
            if (i, a) in memo:
                return memo[(i, a)]
            if a == 0:
                return 1
            if a < 0:
                return 0
            if i >= len(coins):
                return 0

            res = 0
            if a >= coins[i]:
                res += opt(i + 1, a)
                res += opt(i, a - coins[i])

            memo[(i, a)] = res
            return res            

        return opt(0, amount)