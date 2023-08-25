class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        GRAY = 1
        BLACK = 2
        
        states = defaultdict(int)
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
    
        def helper(node: int) -> bool:
            if states[node] == BLACK:
                return True
            
            if states[node] == GRAY:
                return False
            
            if node != destination and not graph[node]:
                return False
            
            states[node] = GRAY
            for nei in graph[node]:
                if not helper(nei):
                    return False
            states[node] = BLACK
            
            return True
        
        return helper(source)