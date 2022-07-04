class Solution {
    public int coinChange(int[] coins, int amount) {
        int ans = helper(
            coins, amount, new int[amount + 1]
        );
        
        return (ans == Integer.MAX_VALUE) ? -1 : ans;
    }
    
    private int helper(int[] coins, int remaining, int[] dp) {
        if (remaining < 0) 
            return Integer.MAX_VALUE;
        
        if (remaining == 0)
            return 0;
        
        if (dp[remaining] == 0){
            int ans = Integer.MAX_VALUE;
            for (int coin : coins)
                ans = Math.min(ans, helper(coins, remaining - coin, dp));
            dp[remaining] = (ans == Integer.MAX_VALUE) ? Integer.MAX_VALUE : ans + 1;
        }
        
        return dp[remaining];
    }
}