class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        heap, nodes, max_time = [(0, k)], defaultdict(int), 0
        while heap:
            time, src = heappop(heap)
            if src not in nodes:
                nodes[src] = time
                max_time = max(max_time, time)
                for w, dst in graph[src]:
                    heappush(heap, (time + w, dst))
        return -1 if len(nodes) != n else max_time