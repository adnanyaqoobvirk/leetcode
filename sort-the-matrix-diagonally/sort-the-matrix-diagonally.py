from heapq import heapify, heappop

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        def countingSort(arr: List[int], start: int, end: int) -> None:
            digit_count = {}
            for num in arr:
                digit_count[num] = digit_count.get(num, 0) + 1
            
            i = 0
            for num in range(start, end + 1):
                for _ in range(digit_count.get(num, 0)):
                    arr[i] = num
                    i += 1
        
        def sortDiagonal(row: int, col: int) -> None:
            diagonal = []
            diagonal_size = min(m - row, n - col)
            
            for i in range(diagonal_size):
                diagonal.append(mat[row + i][col + i])
                
            countingSort(diagonal, 1, 100)
            
            for i in range(diagonal_size):
                mat[row + i][col + i] = diagonal[i]
        
        m = len(mat)
        n = len(mat[0])
        
        for col in range(n):
            sortDiagonal(0, col)
        
        for row in range(1, m):
            sortDiagonal(row, 0)
            
        return mat
            