class UF:
    def __init__(self, n: int) -> None:
        self.roots = [i for i in range(n)]
        self.rank = [0] * n
    
    def find(self, node: int) -> int:
        if self.roots[node] != node:
            self.roots[node] = self.find(self.roots[node])
        return self.roots[node]
    
    def union(self, node1: int, node2: int) -> bool:
        root1, root2 = self.find(node1), self.find(node2)
        if root1 == root2:
            return False
        
        if self.rank[root1] > self.rank[root2]:
            self.roots[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.roots[root1] = root2
        else:
            self.roots[root1] = root2
            self.rank[root2] += 1
            
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for src, dst in edges:
            nodes.add(src)
            nodes.add(dst)
        
        uf, extra = UF(len(nodes) + 1), None
        for src, dst in edges:
            if not uf.union(src, dst):
                extra = [src, dst]
        return extra