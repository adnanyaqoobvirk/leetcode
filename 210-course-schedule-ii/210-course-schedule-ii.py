class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegrees = defaultdict(list), defaultdict(int)
        for dst, src in prerequisites:
            graph[src].append(dst)
            indegrees[dst] += 1
        
        q, ans = [k for k in range(numCourses) if indegrees[k] == 0], []
        while q:
            nq = []
            for src in q:
                ans.append(src)
                for dst in graph[src]:
                    indegrees[dst] -= 1
                    if indegrees[dst] == 0:
                        nq.append(dst)
            q = nq
        return [] if len(ans) != numCourses else ans