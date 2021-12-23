class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph, indegrees = defaultdict(list), {}
        for src, dst in prerequisites:
            graph[dst].append(src)
            indegrees[src] = indegrees.get(src, 0) + 1
        
        q = []
        for i in range(numCourses):
            if indegrees.get(i, 0) == 0:
                q.append(i)
        
        while q:
            nq = []
            for node in q:
                for dst in graph[node]:
                    indegree = indegrees.get(dst, 0)
                    if indegree == 1:
                        del indegrees[dst]
                        nq.append(dst)
                    elif indegree > 1:
                        indegrees[dst] -= 1
            q = nq
        return len(indegrees) == 0
        
        
                        