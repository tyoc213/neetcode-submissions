from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def avanzar(n) -> int:
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            return avanzar(n-2) + avanzar(n-1)
        return avanzar(n)