from collections import defaultdict

List = list
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = defaultdict(list)
        for idx, i in enumerate(nums):
            d[i].append(idx)
        for v in d:
            missing = target - v
            if missing in d:
                if v != missing:
                    l = [None, None]
                    l[0] = d[v].pop()
                    l[1] = d[missing].pop()
                    return sorted(l)
                elif v == missing and len(d[v]) >= 2:
                    l = [None, None]
                    l[0] = d[v].pop()
                    l[1] = d[missing].pop()
                    return sorted(l)