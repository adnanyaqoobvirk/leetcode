class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph, indegrees = defaultdict(list), defaultdict(int)
        for p, c in relations:
            graph[p].append(c)
            indegrees[c] += 1
        
        q, ans = [c for c in range(n) if indegrees[c] == 0], 0
        while q:
            nq = []
            
            for p in q:
                for c in graph[p]:
                    indegrees[c] -= 1
                    if indegrees[c] == 0:
                        nq.append(c)
            q = nq
            ans += 1
        for c, degree in indegrees.items():
            if degree > 0:
                return -1
        return ans