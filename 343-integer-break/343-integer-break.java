class Solution {
    public int integerBreak(int n) {
        int[] dp = new int[n + 1];
        dp[0] = 1;
        for(int num = 1; num < n; num++)
            for(int remaining = num; remaining <= n; remaining++)
                dp[remaining] = Math.max(
                    num * dp[remaining - num], 
                    dp[remaining]
                );
        return dp[n];
    }
}