class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat
        
        nmat = [[0] * c for _ in range(r)]
        
        i = j = 0
        for row in mat:
            for col in row:
                nmat[i][j] = col
                if j == c - 1:
                    i += 1
                    j = 0
                else:
                    j += 1
        return nmat