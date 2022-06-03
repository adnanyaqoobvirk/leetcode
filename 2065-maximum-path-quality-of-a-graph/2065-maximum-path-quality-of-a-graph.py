class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        def helper(curr: int, time: int, quality: int) -> int:
            if time > maxTime:
                return 0
            
            max_quality = quality if curr == 0 else 0
            for neighbor, ntime in graph[curr]:
                if neighbor not in path:
                    quality += values[neighbor]
                    path[neighbor] = 0
                    
                path[neighbor] += 1
                max_quality = max(max_quality, helper(neighbor, time + ntime, quality))
                path[neighbor] -= 1
                
                if path[neighbor] == 0:
                    del path[neighbor]
                    quality -= values[neighbor]
            return max_quality
        
        graph = defaultdict(list)
        for src, dst, time in edges:
            graph[src].append((dst, time))
            graph[dst].append((src, time))
        
        path = {0: 1}
        return helper(0, 0, values[0])