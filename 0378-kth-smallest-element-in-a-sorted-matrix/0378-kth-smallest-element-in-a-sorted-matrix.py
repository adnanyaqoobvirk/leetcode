class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def possible(guess):
            count = 0
            j = 0
            i = n - 1
            while j < n and i >= 0:
                if guess >= matrix[i][j]:
                    count += i + 1
                    j += 1
                else:
                    i -= 1
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