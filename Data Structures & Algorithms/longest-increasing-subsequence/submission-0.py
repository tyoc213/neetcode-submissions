from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        @cache
        def dfs(i, prev):
            if i>=len(nums): return 0

            lis = dfs(i+1, prev)

            if prev == -1 or nums[prev] < nums[i]:
                lis = max(lis, 1+dfs(i+1, i))
            return lis

        return dfs(0, -1)

