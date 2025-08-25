class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diags = [deque() for _ in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                if i + j & 1:
                    diags[i + j].append(mat[i][j])
                else:
                    diags[i + j].appendleft(mat[i][j])
        return [diags[i][j] for i in range(m + n - 1) for j in range(len(diags[i]))]