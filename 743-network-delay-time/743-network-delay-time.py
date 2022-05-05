class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
            
        q, node_times = [k], defaultdict(lambda: float('inf'))
        node_times[k] = 0
        while q:
            nq = []
            for src in q:
                for dst, time in graph[src]:
                    if node_times[dst] > (node_times[src] + time):
                        node_times[dst] = node_times[src] + time
                        nq.append(dst)
            q = nq
        
        if len(node_times) != n:
            return -1
        
        return max(node_times.values())