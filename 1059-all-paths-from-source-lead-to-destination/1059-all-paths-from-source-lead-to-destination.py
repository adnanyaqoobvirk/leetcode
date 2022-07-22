class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(set)
        indegrees = defaultdict(int)
        for src, dst in edges:
            graph[src].add(dst)
            indegrees[dst] += 1
            
        if graph[destination]:
            return False
        
        q = [source]
        while q:
            nq = []
            for curr in q:
                if not graph[curr] and curr != destination:
                    return False
            
                if indegrees[curr] < 0 and curr != destination:
                    return False
                
                for child in graph[curr]:
                    indegrees[child] -= 1
                    nq.append(child)
            q = nq
        return True