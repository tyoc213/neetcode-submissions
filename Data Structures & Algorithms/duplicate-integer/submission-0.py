class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = {}
        for i in nums:
            if i in d:
                return True
            else:
                d[i] = 1
        return False


if __name__ == "__main__":
    s = Solution()
    assert(True == s.hasDuplicate([1,2,3,3]))
    assert(False == s.hasDuplicate([1,2,3,4]))
