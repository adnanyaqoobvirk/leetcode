class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [0] * n
        
        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1 == p2:
                return
            
            if rank[p1] == rank[p2]:
                parent[p2] = p1
                rank[p1] += 1
            elif rank[p1] > rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
        
        for src, dst in edges:
            union(src, dst)
        
        return len({find(node) for node in range(n)})