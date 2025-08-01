class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for _ in range(numRows - 1):
            row = [1]
            for j in range(len(ans[-1]) - 1):
                row.append(ans[-1][j] + ans[-1][j + 1])
            row.append(1)
            ans.append(row)
        return ans