class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        ans = []
        for col in range(n):
            r, c = 0, col
            while r < m:
                if grid[r][c] == 1:
                    if c == n - 1 or grid[r][c + 1] == -1:
                        ans.append(-1)
                        break
                    else:
                        r += 1
                        c += 1
                else:
                    if c == 0 or grid[r][c - 1] == 1:
                        ans.append(-1)
                        break
                    else:
                        r += 1
                        c -= 1
            else:
                ans.append(c)
        return ans