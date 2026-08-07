class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl,l=0,0
        used = set()
        for r in range(len(s)):
            while s[r] in used:
                used.remove(s[l])
                l += 1
            used.add(s[r])
            maxl = max(maxl, r-l+1)
        return maxl

