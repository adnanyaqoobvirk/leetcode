class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def possible(guess):
            count = 0
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] <= guess:
                        count += 1
            return count
        
        n = len(matrix)
        lo, hi = matrix[0][0] - 1, matrix[n - 1][n - 1]
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            
            if possible(mid) >= k:
                hi = mid
            else:
                lo = mid
        return hi