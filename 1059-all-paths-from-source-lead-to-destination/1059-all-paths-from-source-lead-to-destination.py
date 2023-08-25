class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def helper(node: int) -> bool:
            if seen[node] == 2:
                return True
            
            if seen[node] == 1:
                return False
            
            if node != destination and not graph[node]:
                return False
            
            seen[node] = 1
            for nei in graph[node]:
                if not helper(nei):
                    return False
            seen[node] = 2
            
            return True
        
        seen = defaultdict(int)
        
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            
        return helper(source)