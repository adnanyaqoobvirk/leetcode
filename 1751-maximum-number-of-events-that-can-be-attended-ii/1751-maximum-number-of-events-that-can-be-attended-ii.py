class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        @cache
        def dp(i: int, c: int, s: bool) -> int:
            if i >= n or c >= k:
                return 0
            
            if s:
                if i not in nmap:
                    return events[i][2]
                return events[i][2] + max(dp(nmap[i], c + 1, True), dp(nmap[i], c + 1, False))
            else:
                return max(dp(i + 1, c, True), dp(i + 1, c, False))
        
        n = len(events)
        events.sort()
        
        nmap = {}
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
                
        return max(dp(0, 0, True), dp(0, 0, False))