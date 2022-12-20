class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        seen = set()
        q = [start]
        while q:
            nq = []
            for v in q:
                seen.add(v)
                if v == end:
                    return True
                for d in graph[v]:
                    if d not in seen:
                        nq.append(d)
            q = nq
        return False