class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(curr: int) -> bool:
            if curr in safe:
                return True
            
            if curr in seen:
                return False
            
            seen.add(curr)
            
            is_safe = True
            for nei in graph[curr]:
                is_safe = is_safe and dfs(nei)
            
            if is_safe:
                safe.add(curr)
            
            seen.remove(curr)
            
            return is_safe
            
        n, seen, safe = len(graph), set(), set()
        for i in range(n):
            dfs(i)
        
        return sorted(safe)