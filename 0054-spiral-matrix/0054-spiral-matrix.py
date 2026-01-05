class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def traverse(i: int, j: int, k: int, l: int) -> None:
            if i > k or j > l:
                return 
                
            if i == k:
                for y in range(j, l + 1):
                    result.append(matrix[i][y])
                return

            if j == l:
                for x in range(i, k + 1):
                    result.append(matrix[x][j])
                return
            
            for y in range(j, l + 1):
                result.append(matrix[i][y])
            
            for x in range(i + 1, k + 1):
                result.append(matrix[x][l])
            
            for y in reversed(range(j, l)):
                result.append(matrix[k][y])
            
            for x in reversed(range(i + 1, k)):
                result.append(matrix[x][j])
            
            traverse(i + 1, j + 1, k - 1, l - 1)
        
        m, n = len(matrix), len(matrix[0])
        result = []
        traverse(0, 0, m - 1, n - 1)
        return result