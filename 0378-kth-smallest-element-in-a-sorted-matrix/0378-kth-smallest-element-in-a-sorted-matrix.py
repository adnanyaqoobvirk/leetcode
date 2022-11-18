class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        if k == n**2:
            return matrix[n - 1][n - 1]
        
        h = []
        for row in matrix:
            for col in row:
                heappush(h, -col)
                if len(h) > k:
                    heappop(h)
        return -heappop(h)