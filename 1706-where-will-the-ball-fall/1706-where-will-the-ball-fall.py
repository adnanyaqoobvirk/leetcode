class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        ans = [-1] * n
        for c in range(n):
            j = c
            for r in range(m):
                if grid[r][j] == 1:
                    if j == n - 1 or grid[r][j + 1] == -1:
                        break
                    j += 1
                else:
                    if j == 0 or grid[r][j - 1] == 1:
                        break
                    j -= 1
            else:
                ans[c] = j
        return ans