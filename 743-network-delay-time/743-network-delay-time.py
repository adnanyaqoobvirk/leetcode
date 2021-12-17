class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        nodes, visited, minheap = {i: float('inf') for i in range(1, n + 1)}, set(), [(0, k)]
        nodes[k] = 0
        while minheap:
            distance, curr_node = heappop(minheap)
            if curr_node not in visited:
                if distance == float('inf'):
                    return -1

                for dst, time in graph[curr_node]:
                    nodes[dst] = min(nodes[dst], nodes[curr_node] + time)
                    heappush(minheap, (nodes[dst], dst))

                visited.add(curr_node)
        ans = max(nodes.values())
        return -1 if ans == float('inf') else ans