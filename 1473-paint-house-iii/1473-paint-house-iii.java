class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        int[][][] dp = new int[m + 1][target + 1][n + 1];
        for(int i = 0; i <= m; i++)
            for(int j = 0; j <= target; j++)
                for(int k = 0; k <= n; k++)
                    dp[i][j][k] = -1;
        
        int res = helper(houses, cost, m, n, target, 0, 0, dp);
        return res == Integer.MAX_VALUE ? -1 : res;
    }
    
    private int helper(int[] houses, int[][] cost, int m, int n, int nhs, int i, int pcolor, int[][][] dp){
        if(i == m)
            return nhs == 0 ? 0 : Integer.MAX_VALUE;
        
        if(nhs < 0)
            return Integer.MAX_VALUE;
        
        if(dp[i][nhs][pcolor] != -1)
            return dp[i][nhs][pcolor];
        
        if(houses[i] != 0)
            dp[i][nhs][pcolor] = helper(
                houses, cost, m, n,
                pcolor != houses[i] ? nhs - 1 : nhs,
                i + 1, houses[i], dp
            );
        else{
            dp[i][nhs][pcolor] = Integer.MAX_VALUE;
            for(int j = 0; j < n; j++){
                int res = helper(
                    houses, cost, m, n,
                    pcolor != j + 1 ? nhs - 1 : nhs,
                    i + 1, j + 1, dp
                );

                if(res != Integer.MAX_VALUE)
                    dp[i][nhs][pcolor] = Math.min(
                        dp[i][nhs][pcolor],
                        cost[i][j] + res
                    );
            } 
        }
        return dp[i][nhs][pcolor];
    }
}