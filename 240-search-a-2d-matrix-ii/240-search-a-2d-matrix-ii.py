class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(min(m, n)):
            # searching in the row
            lo, hi = i, n - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            # searching in the column
            lo, hi = i, m - 1
            while lo <= hi:
                mid = lo + (hi - lo) // 2
                if matrix[mid][i] == target:
                    return True
                elif matrix[mid][i] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return False