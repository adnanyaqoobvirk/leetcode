class DisjointSet:
    def __init__(self, variables: Set[str]) -> None:
        self.vmap = {v: [v, 1] for v in variables}
        
    def find(self, v: str) -> List[Any]:
        if v in self.vmap:
            i, w = self.vmap[v]
            if i != v:
                ni, nw = self.find(i)
                self.vmap[v] = [ni, nw * w]
            return self.vmap[v]
        else:
            return [None, None]
        
    def union(self, v1: str, v2: str, v: int) -> None:
        (pv1i, pv1w), (pv2i, pv2w) = self.find(v1), self.find(v2)
        if pv1i != pv2i:
            self.vmap[pv1i] = [pv2i, v * pv2w / pv1w]
        
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        variables = set()
        for A, B in equations:
            variables.add(A)
            variables.add(B)
            
        ds = DisjointSet(variables)
        for (A, B), V in zip(equations, values):
            ds.union(A, B, V)
        
        ans = []
        for C, D in queries:
            (pci, pcw), (pdi, pdw) = ds.find(C), ds.find(D)
            if pci is not None and pdi is not None and pci == pdi:
                ans.append(pcw / pdw)
            else:
                ans.append(-1.0)
        return ans
            