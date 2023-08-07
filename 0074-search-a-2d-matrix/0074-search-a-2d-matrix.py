class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        l, h = 0, m * n - 1
        while l <= h:
            m = l + h >> 1
            
            r, c = m // n, m % n
            
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                h = m - 1
            else:
                l = m + 1
                
        return False