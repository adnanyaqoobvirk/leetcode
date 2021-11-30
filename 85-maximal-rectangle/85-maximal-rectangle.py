class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m = len(matrix), 0 if len(matrix) == 0 else len(matrix[0])
        
        dp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    dp[i][j] = dp[i][j - 1] + 1
        
        ans = 0
        for k in reversed(range(n)):
            for j in reversed(range(m)):
                col_min = 200
                for i in reversed(range(n - k)):
                    col_min = min(dp[i][j], col_min)
                    if col_min == 0:
                        break
                    ans = max(ans, col_min * (n - k - i))
        return ans
                    
                    