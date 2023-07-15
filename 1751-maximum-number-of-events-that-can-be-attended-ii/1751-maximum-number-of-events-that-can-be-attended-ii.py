class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dp(i: int, c: int) -> int:
            if i >= n or c >= k:
                return 0
                
            return max(
                dp(i + 1, c), events[i][2] + 
                (0 if nmap[i] == -1 else dp(nmap[i], c + 1))
            )
        
        n = len(events)
        events.sort()
        
        nmap = [-1] * n
        for i in range(n):
            l, r = i, n - 1
            while l + 1 < r:
                m = l + r >> 1
                if events[m][0] > events[i][1]:
                    r = m
                else:
                    l = m
            if events[r][0] > events[i][1]:
                nmap[i] = r
                
        return dp(0, 0)