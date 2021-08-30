class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        counts = {}
        for j in range(n):
            for i in range(m):
                count = counts.get(mat[i][j], 0) + 1
                if count == m:
                    return mat[i][j]
                counts[mat[i][j]] = count
        return -1