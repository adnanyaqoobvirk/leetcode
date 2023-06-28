class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
        ans = [[0] * n for _ in range(m)]
                    
        smat2 = []
        for i in range(k):
            smat2.append([])
            for j in range(n):
                if mat2[i][j] != 0:
                    smat2[-1].append((j, mat2[i][j]))
        
        for i in range(m):
            for j in range(k):
                if mat1[i][j] != 0:
                    for x, v in smat2[j]:
                        ans[i][x] += v * mat1[i][j]
        return ans