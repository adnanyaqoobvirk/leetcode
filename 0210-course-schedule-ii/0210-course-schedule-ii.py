class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegrees = defaultdict(int)
        graph = defaultdict(list)
        for dst, src in prerequisites:
            indegrees[dst] += 1
            graph[src].append(dst)
        
        res = []
        q = [i for i in range(numCourses) if indegrees[i] == 0]
        while q:
            nq = []
            
            for src in q:
                res.append(src)
                
                for dst in graph[src]:
                    indegrees[dst] -= 1
                    
                    
                    if indegrees[dst] == 0:
                        nq.append(dst)
            q = nq
        return res if len(res) == numCourses else []