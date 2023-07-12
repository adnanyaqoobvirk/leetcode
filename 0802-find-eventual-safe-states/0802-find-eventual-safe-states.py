class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(curr: int) -> bool:
            if curr in safe:
                return safe[curr]
            
            safe[curr] = False
            
            is_safe = True
            for nei in graph[curr]:
                is_safe = is_safe and dfs(nei)
            
            safe[curr] = is_safe
            
            return is_safe
            
        safe, ans = {}, []
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        
        return ans