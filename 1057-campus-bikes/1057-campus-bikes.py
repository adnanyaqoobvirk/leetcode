class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        def manhattan(x1, x2, y1, y2) -> int:
            return abs(x1 - x2) + abs(y1 - y2)
        
        pairs = []
        for i, (wx, wy) in enumerate(workers):
            for j, (bx, by) in enumerate(bikes):
                pairs.append((manhattan(wx, bx, wy, by), i, j))
        
        pairs.sort()
        ans = [-1] * len(workers)
        bs = [-1] * len(bikes)
        for _, wi, bi in pairs:
            if ans[wi] == -1 and bs[bi] == -1:
                ans[wi] = bi
                bs[bi] = wi
        return ans