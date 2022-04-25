class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getCounts(guess: int) -> Tuple[List[Tuple[int, int]], List[Tuple[int, int]]]:
            closer, farther = [], []
            for d, i in dpoints:
                if d <= guess:
                    closer.append((d, i))
                else:
                    farther.append((d, i))
            return closer, farther
        
        dpoints, maxd = [], float('-inf')
        for i, (x, y) in enumerate(points):
            d = x**2 + y**2
            maxd = max(maxd, d)
            dpoints.append((d, i))
        
        lo, hi, ans = 0, maxd, []
        while k:
            mid = lo + (hi - lo) / 2
            closer, farther = getCounts(mid)
            if len(closer) > k:
                hi = mid
                dpoints = closer
            else:
                lo = mid
                for _, i in closer:
                    ans.append(points[i])
                k -= len(closer)
                dpoints = farther
        return ans
        
        