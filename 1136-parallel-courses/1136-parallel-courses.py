class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for src, dst in relations:
            graph[src].append(dst)
            indegrees[dst] += 1
    
        q = [i for i in range(1, n + 1) if indegrees[i] == 0]
        semesters, seen = 0, set(q)
        while q:
            nq = []
            for src in q:
                for dst in graph[src]:
                    indegrees[dst] -= 1
                    
                    if indegrees[dst] == 0:
                        nq.append(dst)
                        seen.add(dst)
            q = nq
            semesters += 1
        return semesters if len(seen) == n else -1