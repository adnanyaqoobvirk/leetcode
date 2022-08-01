class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        def rotate():
            for i in range(n):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
            
            for i in range(n):
                mat[i].reverse()
        
        for _ in range(4):
            rotate()
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        break
                else:
                    continue
                break
            else:
                return True
        return False