class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if k * k == n:
            return matrix[n - 1][n - 1]
        
        h = []
        for i in range(n):
            for j in range(n):
                if len(h) < k:
                    heappush(h, -matrix[i][j])
                else:
                    heappushpop(h, -matrix[i][j])
        return -h[0]