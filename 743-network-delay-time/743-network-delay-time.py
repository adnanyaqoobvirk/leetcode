class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dst, time in times:
            graph[src].append((dst, time))
            
        stack, node_times = [k], defaultdict(lambda: float('inf'))
        node_times[k] = 0
        while stack:
            src = stack.pop()
            for dst, time in graph[src]:
                if node_times[dst] > (node_times[src] + time):
                    node_times[dst] = node_times[src] + time
                    stack.append(dst)
        
        if len(node_times) != n:
            return -1
        
        return max(node_times.values())