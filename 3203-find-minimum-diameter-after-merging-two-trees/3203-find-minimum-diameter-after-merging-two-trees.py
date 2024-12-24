class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getDiameter(g: Dict[int, List[int]]) -> int:
            if not g:
                return 0

            q = [0]
            seen = set([0])
            while q:
                nq = []
                for node in q:
                    for nei in g[node]:
                        if nei not in seen:
                            nq.append(nei)
                            seen.add(nei)
                if not nq:
                    res = q[0]
                q = nq

            q = [res]
            seen = set([res])
            dia = -1
            while q:
                nq = []
                for node in q:
                    for nei in g[node]:
                        if nei not in seen:
                            nq.append(nei)
                            seen.add(nei)
                q = nq
                dia += 1
            return dia

        def getTree(edges: List[List[int]]) -> Dict[int, List[int]]:
            t = defaultdict(list)
            for src, dst in edges:
                t[src].append(dst)
                t[dst].append(src)
            return t

        return ceil(getDiameter(getTree(edges1)) / 2) + ceil(getDiameter(getTree(edges2)) / 2) + 1