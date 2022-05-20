class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def helper(curr: int) -> bool:
            if seen[curr] == 1:
                return False
            
            if seen[curr] == 2:
                return True
            
            seen[curr] += 1
            
            is_safe = True
            for neighbor in graph[curr]:
                if not helper(neighbor):
                    is_safe = False
            
            if not is_safe:
                safe_nodes.discard(curr)
                return False
            
            seen[curr] += 1
            return True
        
        safe_nodes, seen = {node for node in range(len(graph))}, defaultdict(int)
        for node in range(len(graph)):
            if seen[node] == 0:
                helper(node)
        return sorted(safe_nodes)