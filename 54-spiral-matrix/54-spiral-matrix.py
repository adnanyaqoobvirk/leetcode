class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        pos = 0
        for n, m in zip(range(len(matrix), 0, -2), range(len(matrix[0]), 0, -2)):
            for j in range(pos, pos + m):
                ans.append(matrix[pos][j])

            for i in range(pos + 1, pos + n):
                ans.append(matrix[i][pos + m - 1])

            if n > 1:
                for j in range(pos + m - 2, pos - 1, -1):
                    ans.append(matrix[pos + n - 1][j])

            if m > 1:
                for i in range(pos + n - 2, pos, -1):
                    ans.append(matrix[i][pos])
            pos += 1
        return ans
        