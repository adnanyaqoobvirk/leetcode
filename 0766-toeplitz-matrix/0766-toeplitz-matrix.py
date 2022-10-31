class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                x, y = i - 1, j - 1
                if 0 <= x < m and 0 <= y < n:
                    if matrix[i][j] != matrix[x][y]:
                        return False
        return True