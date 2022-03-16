class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][-1]:
                lo, hi = 0, n - 1
                while lo <= hi:
                    mid = lo + (hi - lo) // 2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        lo = mid + 1
                    else:
                        hi = mid - 1
        return False