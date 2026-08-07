class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []: return 0
        if len(nums) == 1: return 1
        l = sorted(set(nums))
        if len(nums) == 0: return 1

        longestFound = 0

        for idx, v in enumerate(l):
            if idx == 0:
                start= 0
            else:
                if l[idx-1]+1 != l[idx]:
                    if idx-start > longestFound:
                        longestFound = idx-start
                    start = idx
        if idx-start+1>longestFound:
            return idx-start+1
        else:
            return longestFound

