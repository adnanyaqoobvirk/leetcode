class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort(reverse=True)
        h = []
        res = 0
        for i in range(1, max(end for _, end in events) + 1):
            while events and events[-1][0] <= i:
                start, end = events.pop()
                heappush(h, end)
            while h and h[0] < i:
                heappop(h)
            if h:
                heappop(h)
                res += 1
        return res