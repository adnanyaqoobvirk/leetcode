class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, t in times:
            graph[src].append((dst, t))

        timeMap = defaultdict(lambda: inf)
        timeMap[k] = 0
        earliest = [(0, k)]
        while earliest:
            t, node = heappop(earliest)
            
            for nei, nt in graph[node]:
                if timeMap[nei] > t + nt:
                    heappush(earliest, (t + nt, nei))
                    timeMap[nei] = t + nt
        maxTime = 0
        for i in range(1, n + 1):
            maxTime = max(maxTime, timeMap[i])
        return -1 if maxTime == inf else maxTime