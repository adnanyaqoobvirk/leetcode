class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        if k * k == n:
            return matrix[n - 1][n - 1]
        
        h = []
        for i in range(n):
            for j in range(n):
                heappush(h, -matrix[i][j])
                if len(h) > k:
                    heappop(h)
        return -h[0]