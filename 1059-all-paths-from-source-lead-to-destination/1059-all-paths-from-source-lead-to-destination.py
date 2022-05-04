class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def helper(curr: int) -> bool:
            if not graph[curr] and curr != destination:
                return False
            
            visited[curr] = False
            for node in graph[curr]:
                if node in visited and not visited[node]:
                    return False
                
                if not helper(node):
                    return False
            visited[curr] = True
            return True
        
        graph = defaultdict(set)
        for src, dst in edges:
            graph[src].add(dst)
        
        visited = {}
        return helper(source)
        