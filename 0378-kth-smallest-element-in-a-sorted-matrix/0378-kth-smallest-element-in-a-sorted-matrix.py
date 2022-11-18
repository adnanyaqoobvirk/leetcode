class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        
        sign = -1
        if k > n**2//2:
            sign = 1
            k = n**2 - k + 1

        h = []
        for row in matrix:
            for col in row:
                heappush(h, sign * col)
                if len(h) > k:
                    heappop(h)
        return sign * heappop(h)