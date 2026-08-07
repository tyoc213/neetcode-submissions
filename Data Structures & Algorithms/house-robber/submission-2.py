from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_house(idx):
            if idx >= len(nums):
                return -0
            return nums[idx] + max(rob_house(idx+2), rob_house(idx+3))
        return max(rob_house(0), rob_house(1))

