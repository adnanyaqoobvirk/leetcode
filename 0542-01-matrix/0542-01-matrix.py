class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q, seen = [], set()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))
        
        d, ans = 0, [[0] * n for _ in range(m)]
        while q:
            nq = []
            
            for i, j in q:
                ans[i][j] = d
                
                for t in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= t[0] < m and 0 <= t[1] < n and t not in seen:
                        seen.add(t)
                        nq.append(t)
            d += 1
            q = nq
        return ans