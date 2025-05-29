class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        diags = [[] for _ in range(m + n - 1)]
        for i in range(m):
            for j in range(n):
                diags[i + j].append(mat[i][j])
        r = True
        ans = []
        for i in range(m + n - 1):
            if r:
                ans.extend(diags[i][::-1])
            else:
                ans.extend(diags[i])
            r = not r
        return ans