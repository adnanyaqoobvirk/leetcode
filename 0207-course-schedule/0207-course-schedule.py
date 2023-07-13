class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(curr: int) -> bool:
            if curr in seen:
                return not seen[curr]
        
            seen[curr] = False
            for nei in graph[curr]:
                if dfs(nei):
                    return True
            seen[curr] = True
            
            return False
        
        graph = defaultdict(list)
        for dst, src in prerequisites:
            graph[dst].append(src)
        
        seen = {}
        for i in range(numCourses):
            if dfs(i):
                return False
        return True