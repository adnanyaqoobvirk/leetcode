class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        nodes, minheap = {}, [(0, k)]
        while minheap:
            distance, curr_node = heappop(minheap)
            if curr_node not in nodes:
                nodes[curr_node] = distance
                for dst, time in graph[curr_node]:
                    if dst not in nodes:
                        heappush(minheap, (distance + time, dst))
        return max(nodes.values()) if len(nodes) == n else -1