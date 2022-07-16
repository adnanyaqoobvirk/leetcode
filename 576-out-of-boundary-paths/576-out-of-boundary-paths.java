class Solution {
    private int MOD = 1000000007;
    
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][]  dp = new int[m][n][maxMove];
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
                Arrays.fill(dp[i][j], -1);
        
        return this.helper(m, n, maxMove, dp, startRow, startColumn, 0);
    }
    
    private int helper(int m, int n, int maxMove, int[][][] dp, int x, int y, int moves){
        if(x < 0 || x >= m || y < 0 || y >= n)
            return 1;
        
        if(moves == maxMove)
            return 0;
        
        if(dp[x][y][moves] == -1){
            dp[x][y][moves] = (
                (
                    this.helper(
                        m, n, maxMove, dp, x + 1, y, moves + 1
                    ) + this.helper(
                        m, n, maxMove, dp, x - 1, y, moves + 1
                    )
                ) % MOD + 
                (
                    this.helper(
                        m, n, maxMove, dp, x, y + 1, moves + 1
                    ) + this.helper(
                        m, n, maxMove, dp, x, y - 1, moves + 1
                    )
                ) % MOD
            ) % MOD;
        }
        return dp[x][y][moves];
    }
}