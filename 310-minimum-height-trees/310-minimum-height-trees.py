class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph, indegrees = defaultdict(list), defaultdict(int)
        for s, d in edges:
            graph[s].append(d)
            graph[d].append(s)
            indegrees[d] += 1
            indegrees[s] += 1
        
        q = [node for node in range(n) if indegrees[node] == 1]
        while q:
            nq = []
            for s in q:
                for d in graph[s]:
                    indegrees[d] -= 1
                    if indegrees[d] == 1:
                        nq.append(d)
            if not nq:
                break
            q = nq
        return q