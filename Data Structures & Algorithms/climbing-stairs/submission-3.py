from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1,2,3] + [None] * (n)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        
        if n < 0:
            return -1
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        total = 0
        for i in range(3, n+1):
            dp[i] = dp[i-1]+dp[i-2]
        # @cache
        # def avanzar(n) -> int:
        #     if n <= 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     return avanzar(n-2) + avanzar(n-1)
        # return avanzar(n)
        print(dp)
        return dp[n-1]+dp[n-2]