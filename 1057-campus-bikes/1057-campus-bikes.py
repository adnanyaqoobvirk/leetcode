class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def manhattan(x1, x2, y1, y2) -> int:
            return abs(x1 - x2) + abs(y1 - y2)
        
        min_d, max_d = float('inf'), float('-inf')
        pairs = defaultdict(list)
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                d = manhattan(wx, bx, wy, by)
                pairs[d].append((i, j))
                min_d, max_d = min(min_d, d), max(max_d, d)
        
        ans = [-1] * len(workers)
        bs = [-1] * len(bikes)
        for d in range(min_d, max_d + 1):
            for wi, bi in pairs[d]:
                if ans[wi] == -1 and bs[bi] == -1:
                    ans[wi] = bi
                    bs[bi] = wi
        return ans