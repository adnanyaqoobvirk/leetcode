class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
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
        
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for i in reversed(range(n)):
            for j in reversed(range(k)):
                dp[i][j] = max(
                    dp[i + 1][j],
                    events[i][2] + (0 if nmap[i] == -1 else dp[nmap[i]][j + 1])
                )
        return dp[0][0]