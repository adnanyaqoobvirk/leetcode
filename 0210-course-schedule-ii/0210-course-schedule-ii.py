class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        indegree = defaultdict(int)
        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        
        ordered_courses = []
        q = deque([course for course in range(numCourses) if indegree[course] == 0])
        while q:
            course = q.popleft()
            ordered_courses.append(course)

            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        return ordered_courses if len(ordered_courses) == numCourses else []