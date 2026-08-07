class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def groups(strs: List[str]):
            counts = defaultdict(list)
            for s in strs:
                hash = [0] * 26
                for c in s:
                    hash[ord(c) - ord("a")] += 1
                counts[tuple(hash)].append(s)
            return list(counts.values())
        return groups(strs)