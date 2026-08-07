"""
0 <= cost_i <= 100
2 <= cost.length <= 100
"""

from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def step(total, idx):
            if len(cost) == 2:
                return min(cost[0], cost[1])
            if idx >= len(cost)-1:
                return total
            take = step(cost[idx], idx+1)
            skip = step(cost[idx+1], idx+2)
            return total+min(take, skip)
        return step(0, 0)