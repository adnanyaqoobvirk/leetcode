class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            row = [1]
            for i in range(len(res[-1]) - 1):
                row.append(res[-1][i] + res[-1][i + 1])
            row.append(1)
            res.append(row)
        return res