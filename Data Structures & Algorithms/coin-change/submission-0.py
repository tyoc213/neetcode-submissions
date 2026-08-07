from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def num_change(amount):
            if amount == 0:
                return 0

            res = 1e9
            for c in coins:
                if amount-c >= 0:
                     res = min(res, 1+num_change(amount-c))
            return res
        res = num_change(amount)
        return -1 if res >=1e9 else res

