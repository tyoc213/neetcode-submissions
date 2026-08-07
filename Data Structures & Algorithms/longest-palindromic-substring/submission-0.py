class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend_palindrome(start, end):
            if start-1 < 0 or end+1 >= len(s):
                return start, end
            if s[start-1] == s[end+1]:
                return extend_palindrome(start-1, end+1)
            else:
                return start, end
        longest = ""
        for idx, _ in enumerate(s):
            start, end = extend_palindrome(idx, idx)
            if len(longest) < end-start+1:
                longest = s[start:end+1]

            if idx+1 >= len(s): continue
            start, end = extend_palindrome(idx, idx+1 if s[idx] == s[idx+1] else idx)
            if len(longest) < end-start+1:
                longest = s[start:end+1]
        return longest


