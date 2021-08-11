class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_map = {}
        for i, gsize in enumerate(groupSizes):
            groups = groups_map.setdefault(gsize, [[]])
            if len(groups[-1]) == gsize:
                groups.append([])
            groups[-1].append(i)
        return [group for groups in groups_map.values() for group in groups]