class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return "😉None"
        if strs == [""]: return ""
        return "😉".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "😉None": return []
        parts = s.split("😉")
        return parts

