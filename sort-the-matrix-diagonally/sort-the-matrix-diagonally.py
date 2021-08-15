from heapq import heapify, heappop

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)
        n = len(mat[0])
        diagonals = {}
        
        for row in range(m):
            for col in range(n):
                diagonals.setdefault(row - col, []).append(mat[row][col])
            
        for diagonal in diagonals.values():
            heapify(diagonal)
        
        for row in range(m):
            for col in range(n):
                mat[row][col] = heappop(diagonals[row - col])
        
        return mat
            