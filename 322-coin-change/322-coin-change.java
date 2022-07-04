class Solution {
    public int coinChange(int[] coins, int amount) {
        double ans = helper(coins, 0, amount, new double[coins.length + 1][amount + 1]);
        return ans == Double.POSITIVE_INFINITY ? -1 : (int) ans;
    }
    
    private double helper(int[] coins, int i, int remaining, double[][] dp) {
        if (i == coins.length || remaining < 0) 
            return Double.POSITIVE_INFINITY;
        
        if (remaining == 0)
            return 0.0;
        
        if (dp[i][remaining] == 0.0)
            dp[i][remaining] = Math.min(
                1 + helper(coins, i, remaining - coins[i], dp),
                helper(coins, i + 1, remaining, dp)
            );
        
        return dp[i][remaining];
    }
}