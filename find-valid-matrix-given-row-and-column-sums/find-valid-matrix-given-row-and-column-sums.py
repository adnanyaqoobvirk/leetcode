class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n = len(rowSum)
        m = len(colSum)
        result = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                result[i][j] = min(rowSum[i], colSum[j])
                rowSum[i] -= result[i][j]
                colSum[j] -= result[i][j]
        return result