class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(lambda a: ord('0')<=ord(a)<=ord('9') or ord('A')<=ord(a)<=ord('Z') or ord('a')<=ord(a)<=ord('z'), s)).lower()
        print(s)
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True

