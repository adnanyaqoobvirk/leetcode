class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
            
        heap, node_times = [(0, k)], {}
        while heap:
            stime, src = heappop(heap)
            if src not in node_times:
                node_times[src] = stime
                for dst, time in graph[src]:
                    if dst not in node_times:
                        heappush(heap, (time + stime, dst))
        return max(node_times.values()) if len(node_times) == n else -1