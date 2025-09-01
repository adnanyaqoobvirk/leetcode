class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        @cache
        def dp(pos: int, mask: int) -> int:
            if mask.bit_count() >= n:
                return 0
            
            if pos >= m:
                return inf
            
            res = dp(pos + 1, mask)
            for i in range(n):
                if (1 << i) & mask:
                    continue

                d = abs(bikes[pos][0] - workers[i][0]) + abs(bikes[pos][1] - workers[i][1])
                res = min(res, d + dp(pos + 1, mask | (1 << i)))
            return res

        m = len(bikes)
        n = len(workers)
        return dp(0, 0)