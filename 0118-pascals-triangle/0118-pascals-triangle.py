class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        ans = [[1], [1, 1]]
        for _ in range(2, numRows):
            row = [1]
            for i in range(1, len(ans[-1])):
                row.append(ans[-1][i - 1] + ans[-1][i])
            row.append(1)
            ans.append(row)
        return ans