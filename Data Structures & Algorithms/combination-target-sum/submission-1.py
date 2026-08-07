class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(idx, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if idx>=len(nums) or total > target:
                return
            backtrack(idx, (curr+[nums[idx]]).copy(), total+nums[idx])
            backtrack(idx+1, curr, total)

        backtrack(0,[], 0)
        return res
        