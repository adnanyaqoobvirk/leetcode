class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def recurse(x: int, y:int, n: int, m: int) -> None:
            if n > 0 and m > 0:
                for j in range(y, y + m):
                    ans.append(matrix[x][j])

                for i in range(x + 1, x + n):
                    ans.append(matrix[i][y + m - 1])

                if n > 1:
                    for j in range(y + m - 2, y - 1, -1):
                        ans.append(matrix[x + n - 1][j])

                if m > 1:
                    for i in range(x + n - 2, x, -1):
                        ans.append(matrix[i][y])

                recurse(x + 1, y + 1, n - 2, m - 2)
        
        ans = []
        recurse(0, 0, len(matrix), len(matrix[0]))
        return ans
        