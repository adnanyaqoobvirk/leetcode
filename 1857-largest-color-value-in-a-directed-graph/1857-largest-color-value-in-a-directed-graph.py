class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        d,g,c = Counter(), defaultdict(list), defaultdict(Counter)
        for u, v in edges:
            g[u].append(v)
            d[v] += 1
        q = [u for u in range(len(colors)) if d[u]==0]
        for u in q:
            c[u][colors[u]] += 1
            for v in g[u]:
                c[v] |= c[u]
                d[v] -= 1
                if d[v]==0:
                    q.append(v)
        return sum(d.values()) and -1 or max(max(c[u].values()) for u in c)