class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res, groups = [], defaultdict(list)
        for i, gsize in enumerate(groupSizes):
            groups[gsize].append(i)
            if len(groups[gsize]) == gsize:
                res.append(groups.pop(gsize))
        return res