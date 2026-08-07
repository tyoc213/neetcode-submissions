from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = defaultdict(int)
        d2 = defaultdict(int)
        for i in s:
            d1[i] += 1
        for j in t:
            d2[j] += 1
        return d1 == d2

if __name__ == "__main__":
    s = Solution()
    assert(True == s.isAnagram("racecar", "carrace"))
    assert(False == s.isAnagram("jar", "jam"))
