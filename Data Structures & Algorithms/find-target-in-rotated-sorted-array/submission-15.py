class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, rigth = 0, len(nums)-1

        i = 0
        while left <= rigth:
            mid = (rigth+left)//2

            if nums[left] == target:
                return left
            elif nums[mid] == target:
                return mid
            elif nums[rigth] == target:
                return rigth

            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    rigth = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < target <= nums[rigth]:
                left = mid + 1
            else:
                rigth = mid - 1
        return -1