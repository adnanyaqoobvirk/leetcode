class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q, n, ans = [[0]], len(graph) - 1, []
        while True:
            nq = []
            for p in q:
                if p[-1] != n:
                    for v in graph[p[-1]]:
                        nq.append(p + [v])
                else:
                    ans.append(p)
            if not nq:
                return ans
            else:
                q = nq