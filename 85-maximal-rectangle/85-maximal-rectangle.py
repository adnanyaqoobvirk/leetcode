class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), 0 if len(matrix) == 0 else len(matrix[0])
        
        ans = 0
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j - 1] + 1
                    
                    minarea = float('inf')
                    for k in reversed(range(i + 1)):
                        minarea = min(dp[k][j], minarea)
                        if minarea == 0: break
                        ans = max(ans, minarea * (i - k + 1))
        return ans