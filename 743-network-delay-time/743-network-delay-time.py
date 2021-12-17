class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
        
        nodes, visited = {i: float('inf') for i in range(1, n + 1)}, set()
        nodes[k] = 0
        while len(visited) < n:
            curr_node, distance = -1, float('inf')
            for node, d in nodes.items():
                if node not in visited and d < distance:
                    curr_node, distance = node, d
            
            if distance == float('inf'):
                return -1
            
            for dst, time in graph[curr_node]:
                nodes[dst] = min(nodes[dst], nodes[curr_node] + time)
            
            visited.add(curr_node)
        return max(nodes.values())