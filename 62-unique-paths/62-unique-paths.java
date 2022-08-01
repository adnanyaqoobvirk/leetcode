class Solution {
    public int uniquePaths(int m, int n) {
        return this.helper(m, n, 0, 0, new int[m][n]);
    }
    
    private int helper(int m, int n, int row, int col, int[][] dp){
        if(row >= m || col >= n){
            return 0;
        }
        
        if(row == m - 1 && col == n - 1){
            return 1;
        }
        
        if(dp[row][col] == 0){
            dp[row][col] = helper(m, n, row + 1, col, dp) + helper(m, n, row, col + 1, dp);
        }
        
        return dp[row][col];
    }
}