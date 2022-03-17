class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def helper(top: int, left: int, bottom: int, right: int) -> bool:
            if top > bottom or left > right:
                return False
            elif matrix[top][left] > target or matrix[bottom][right] < target:
                return False
            
            mid = left + (right - left) // 2
            for row in range(top, bottom + 1):
                if matrix[row][mid] == target:
                    return True
                elif matrix[row][mid] > target:
                    break
            return helper(row, left, bottom, mid) or helper(top, mid + 1, row, right)
        m, n = len(matrix), len(matrix[0])
        return helper(0, 0, m - 1, n - 1)