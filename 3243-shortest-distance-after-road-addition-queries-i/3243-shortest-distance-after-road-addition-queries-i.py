class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for i in range(n - 1):
            graph[i].append(i + 1)

        ans = []
        for u, v in queries:
            graph[u].append(v)
            q = [0]
            l = 0
            while q:
                nq = []
                for u in q:
                    if u == n - 1:
                        break
                    for v in graph[u]:
                        nq.append(v)
                else:
                    l += 1
                    q = nq
                    continue
                break
            ans.append(l)
        return ans