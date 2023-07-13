class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees, graph = defaultdict(int), defaultdict(list)
        for a, b in prerequisites:
            indegrees[a] += 1
            graph[b].append(a)
            
        courses, q = [], [i for i in range(numCourses) if indegrees[i] == 0]
        while q:
            nq = []
            for c in q:
                courses.append(c)
                for d in graph[c]:
                    indegrees[d] -= 1
                    if indegrees[d] == 0:
                        nq.append(d)
            q = nq
        return len(courses) == numCourses