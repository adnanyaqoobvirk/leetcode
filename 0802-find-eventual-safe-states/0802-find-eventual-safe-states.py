class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegrees, ograph = defaultdict(int), defaultdict(list)
        for i, node in enumerate(graph):
            outdegrees[i] += len(node)
            for nei in node:
                ograph[nei].append(i)
        
        n = len(graph)
        ans, q = [False] * n, [i for i in range(n) if outdegrees[i] == 0]
        while q:
            nq = []
            for node in q:
                ans[node] = True
                for nei in ograph[node]:
                    outdegrees[nei] -= 1
                    if outdegrees[nei] == 0:
                        nq.append(nei)
            q = nq
        return [i for i in range(n) if ans[i]]