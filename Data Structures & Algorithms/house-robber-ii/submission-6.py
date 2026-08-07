from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_house2(idx, start):
            if idx == len(nums)-1:
                if start == 0:
                    return 0
                else:
                    return nums[idx]
            if idx >= len(nums):
                return 0
            return nums[idx] + max(rob_house2(idx+2, start), rob_house2(idx+3, start))
        if len(nums) == 3:
            return max(max(nums[0], nums[2]), nums[1])
        if len(nums) == 1:
            return nums[0]
        all = [rob_house2(idx,idx) for idx,_ in enumerate(nums)]
        return max(all)

