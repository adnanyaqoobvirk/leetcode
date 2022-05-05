class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_nodes, q = set(), []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh_nodes.add((i, j))
                elif grid[i][j] == 2:
                    q.append((i, j))
                    
        if not fresh_nodes:
            return 0
        
        minutes = -1
        while q:
            nq = []
            
            for i, j in q:
                for indices in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= indices[0] < m and 0 <= indices[1] < n and indices in fresh_nodes:
                        fresh_nodes.remove(indices)
                        nq.append(indices)
            q = nq
            minutes += 1
        return -1 if fresh_nodes else minutes