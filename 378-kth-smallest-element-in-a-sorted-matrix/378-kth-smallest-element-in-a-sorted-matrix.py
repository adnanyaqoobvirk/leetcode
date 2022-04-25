class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        double = n * n
        half = double // 2
        sign, hmax = (-1, k) if k < half else (1, double - k + 1)
        h = []
        for row in matrix:
            for col in row:
                heappush(h, sign * col)
                if len(h) > hmax:
                    heappop(h)
        return sign * h[0]