class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph, indegrees = defaultdict(list), {}
        for src, dst in prerequisites:
            graph[dst].append(src)
            indegrees[src] = indegrees.get(src, 0) + 1
        
        q = []
        for i in range(numCourses):
            if indegrees.get(i, 0) == 0:
                q.append(i)
        
        ans = []
        while q:
            nq = []
            for node in q:
                ans.append(node)
                for dst in graph[node]:
                    indegree = indegrees.get(dst, 0)
                    if indegree == 1:
                        del indegrees[dst]
                        nq.append(dst)
                    elif indegree > 1:
                        indegrees[dst] -= 1
            q = nq
        return ans if len(indegrees) == 0 else []