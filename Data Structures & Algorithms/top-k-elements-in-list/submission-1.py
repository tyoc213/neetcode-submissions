class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for v in nums:
            groups[v] = groups.get(v, 0) + 1
        res = sorted([[groups[k], k] for k in groups], reverse=True)
        return [v for key, v in res][:k]
