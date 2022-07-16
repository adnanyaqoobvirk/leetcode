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
        if(moves == maxMove)
            return 0;
        
        if(dp[x][y][moves] == -1){
            dp[x][y][moves] = 0;
            
            int i = x;
            for(int j : new int[]{y - 1, y + 1}){
                if(0 <= i && i < m && 0 <= j && j < n){
                    dp[x][y][moves] += this.helper(
                        m, n, maxMove, dp, i, j, moves + 1
                    );
                    dp[x][y][moves] %= MOD;
                }
                else
                    dp[x][y][moves]++;
            }
            int j = y;
            for(int xi : new int[]{x - 1, x + 1}){
                if(0 <= xi && xi < m && 0 <= j && j < n){
                    dp[x][y][moves] += this.helper(
                        m, n, maxMove, dp, xi, j, moves + 1
                    );
                    dp[x][y][moves] %= MOD;
                }
                else
                    dp[x][y][moves]++;
            }
        }
        return dp[x][y][moves];
    }
}