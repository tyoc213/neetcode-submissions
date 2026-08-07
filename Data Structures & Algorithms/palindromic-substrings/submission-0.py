class Solution:
    def countSubstrings(self, s: str) -> int:
        def extend_palindrome(start, end):
            if start-1< 0 or end+1 >= len(s):
                return 0
            if s[start-1] == s[end+1]:
                return 1+ extend_palindrome(start-1, end+1)
            else:
                return 0
        total = 0
        for idx, _ in enumerate(s):
            total += extend_palindrome(idx, idx)
            if idx+1 >= len(s): continue
            if s[idx] == s[idx+1]:
                total += 1+extend_palindrome(idx, idx+1)
        return total + len(s)

