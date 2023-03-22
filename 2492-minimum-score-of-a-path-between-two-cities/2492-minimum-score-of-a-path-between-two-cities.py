class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = maxsize
        gr = [[] for _ in range(n+1)]
        for edge in roads:
            gr[edge[0]].append((edge[1], edge[2]))
            gr[edge[1]].append((edge[0], edge[2]))

        vis = [0] * (n+1)
        q = [1]
        vis[1] = 1
        while q:
            nq = []
            for node in q:
                for v, dis in gr[node]:
                    ans = min(ans, dis)
                    if vis[v] == 0:
                        vis[v] = 1
                        nq.append(v)
            q = nq
        return ans