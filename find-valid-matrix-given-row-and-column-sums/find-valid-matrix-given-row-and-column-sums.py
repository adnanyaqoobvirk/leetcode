class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(rowSum)):
            row = []
            for j in range(len(colSum)):
                row.append(min(rowSum[i], colSum[j]))
                rowSum[i] -= row[-1]
                colSum[j] -= row[-1]
            result.append(row)
        return result