class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        for i in range(n):
            sorted_arr = []
            x = 0
            y = i
            while x < m and y < n:
                sorted_arr.append(mat[x][y])
                x += 1
                y += 1
            sorted_arr.sort()
            
            x = 0
            y = i
            while x < m and y < n:
                mat[x][y] = sorted_arr[x]
                x += 1
                y += 1
            
                
        
        for i in range(1, m):
            sorted_arr = []
            x = i
            y = 0
            while x < m and y < n:
                sorted_arr.append(mat[x][y])
                x += 1
                y += 1
            sorted_arr.sort()
            
            x = i
            y = 0
            while x < m and y < n:
                mat[x][y] = sorted_arr[y]
                x += 1
                y += 1
        return mat
            