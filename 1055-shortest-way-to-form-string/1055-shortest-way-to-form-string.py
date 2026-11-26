class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        index = defaultdict(list)
        for i in range(len(source)):
            index[source[i]].append(i)
        
        min_ss_count = 1
        j = 0
        for c in target:
            if not index[c]:
                return -1

            idx = bisect_left(index[c], j)

            if idx == len(index[c]):
                min_ss_count += 1
                j = index[c][0] + 1
            else:
                j = index[c][idx] + 1
        return min_ss_count