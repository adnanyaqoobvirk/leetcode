class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def helper(curr: int, time: int, quality: int) -> None:
            if time <= maxTime:
                if curr == 0:
                    nonlocal max_quality
                    max_quality = max(max_quality, quality)

                for neighbor, ntime in graph[curr]:
                    if neighbor not in path:
                        quality += values[neighbor]
                    path[neighbor] += 1
                    helper(neighbor, time + ntime, quality)
                    path[neighbor] -= 1
                    if path[neighbor] == 0:
                        del path[neighbor]
                        quality -= values[neighbor]
                        
        graph = defaultdict(list)
        for src, dst, time in edges:
            graph[src].append((dst, time))
            graph[dst].append((src, time))
        
        max_quality, path = 0, defaultdict(int)
        path[0] += 1
        helper(0, 0, values[0])
        return max_quality