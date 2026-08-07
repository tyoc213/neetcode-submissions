class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxl = 0
        charset = set(s)

        for c in charset:
            same, l = 0,0
            for r in range(len(s)):
                if s[r] == c:
                    same += 1

                while (r-l+1) - same > k:
                    if s[l] == c:
                        same -=1
                    l += 1

                maxl = max(maxl, r-l+1)
        return maxl