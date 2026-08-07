class Solution:
    def numDecodings(self, s: str) -> int:
        def decode(idx):
            if idx >= len(s): return 1
            if s[idx] == '0': return 0

            res = decode(idx+1)
            if idx+1<len(s):
                if s[idx] == '1'or (s[idx] == '2' and s[idx+1] < '7'):
                    res += decode(idx+2)
            return res
        res = decode(0)
        return res

