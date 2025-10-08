class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(guess: float) -> bool:
            scounts = 0
            for i in range(len(diffs)):
                if diffs[i] <= guess:
                    continue
                
                scounts += ceil(diffs[i] / guess) - 1
                if scounts > k:
                    return False
            return True

        e = 10**-6
        diffs = []
        max_diff = 0
        for i in range(1, len(stations)):
            diff = stations[i] - stations[i - 1]
            diffs.append(diff)
            max_diff = max(max_diff, diff)
        
        lo, hi = 0, max_diff
        while hi - lo > e:
            mid = (lo + hi) / 2

            if possible(mid):
                hi = mid
            else:
                lo = mid
        return hi