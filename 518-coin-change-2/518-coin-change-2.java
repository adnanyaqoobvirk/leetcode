class Solution {
    public int change(int amount, int[] coins) {
        int[][] dp = new int[coins.length + 1][amount + 1];
        for(int i = 0; i < coins.length + 1; i++)
            Arrays.fill(dp[i], -1);
            
        return helper(
            coins, 0, amount, dp
        );
    }
    
    private int helper(int[] coins, int pos, int remaining, int[][] dp){
        if (remaining == 0)
            return 1;
        
        if (pos == coins.length || remaining < 0)
            return 0;
        
        if (dp[pos][remaining] == -1)
            dp[pos][remaining] = helper(
                coins, pos, remaining - coins[pos], dp
            ) + helper(coins, pos + 1, remaining, dp);
        
        return dp[pos][remaining];
    }
}