from heapq import heapify, heappop

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def sortDiagonal(row: int, col: int) -> None:
            diagonal = []
            diagonal_size = min(m - row, n - col)
            
            for i in range(diagonal_size):
                diagonal.append(mat[row + i][col + i])
                
            diagonal.sort()
            
            for i in range(diagonal_size):
                mat[row + i][col + i] = diagonal[i]
        
        m = len(mat)
        n = len(mat[0])
        
        for col in range(n):
            sortDiagonal(0, col)
        
        for row in range(1, m):
            sortDiagonal(row, 0)
            
        return mat
            