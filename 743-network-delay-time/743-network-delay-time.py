class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))
        
        q, max_time, nodes = [(k, 0)], 0, defaultdict(lambda: float('inf'))
        while q:
            nq = []
            for src, time in q:
                nodes[src] = min(nodes[src], time)
                for w, dst in graph[src]:
                    if time + w < nodes[dst]:
                        nq.append((dst, time + w))
            q = nq
        return -1 if len(nodes) != n else max(nodes.values())