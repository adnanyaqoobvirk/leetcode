class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(curr: int) -> None:
            if curr not in courses and indegrees[curr] == 0:
                courses.add(curr)
                
                for nei in graph[curr]:
                    indegrees[nei] -= 1
                    dfs(nei)
        
        indegrees, graph = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)
            
        courses = set()
        for i in range(numCourses):
            dfs(i)
        return len(courses) == numCourses