class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
            
        nodes = set(range(n))
        res = 0
        while nodes:
            q = [nodes.pop()]
            while q:
                nq = []
                for node in q:
                    for nei in graph[node]:
                        if nei in nodes:
                            nq.append(nei)
                            nodes.remove(nei)
                q = nq
            res += 1
        return res