class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = {i:i for i in range(n)}
        
        def find(node):
            if uf[node] != node:
                uf[node] = find(uf[node])
            return uf[node]
        
        def union(node1, node2):
            uf[find(node2)] = find(node1)
            
        for src, dst in edges:
            union(src, dst)
        
        return len(set(find(i) for i in range(n)))