class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(lambda: [[]])
        for i, gsize in enumerate(groupSizes):
            glist = groups[gsize]
            if len(glist[-1]) == gsize:
                glist.append([])
            glist[-1].append(i)
        
        res = []
        for glist in groups.values():
            res.extend(glist)
        return res