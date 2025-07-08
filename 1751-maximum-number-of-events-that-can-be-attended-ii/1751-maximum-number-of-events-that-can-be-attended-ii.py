class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dp(i: int, r: int) -> int:
            if r <= 0 or i >= n:
                return 0

            lo, hi = i, n - 1
            while lo + 1 < hi:
                mid = lo + (hi - lo) // 2

                if events[mid][0] > events[i][1]: 
                    hi = mid
                else:
                    lo = mid

            return max(
                events[i][2] + dp(hi if events[hi][0] > events[i][1] else n, r - 1),
                dp(i + 1, r)
            )
        n = len(events)
        events.sort()
        return dp(0, k)