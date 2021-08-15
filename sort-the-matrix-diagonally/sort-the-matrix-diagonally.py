from heapq import heapify, heappop

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(n):
            arr = []
            x = 0
            y = i
            while x < m and y < n:
                arr.append(mat[x][y])
                x += 1
                y += 1
            heapify(arr)
            
            x = 0
            y = i
            while x < m and y < n:
                mat[x][y] = heappop(arr)
                x += 1
                y += 1
            
        for i in range(1, m):
            arr = []
            x = i
            y = 0
            while x < m and y < n:
                arr.append(mat[x][y])
                x += 1
                y += 1
            heapify(arr)
            
            x = i
            y = 0
            while x < m and y < n:
                mat[x][y] = heappop(arr)
                x += 1
                y += 1
        return mat
            