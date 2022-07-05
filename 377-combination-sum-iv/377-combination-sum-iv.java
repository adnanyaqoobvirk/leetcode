class Solution {
    public int combinationSum4(int[] nums, int target) {
        int[] dp = new int[target + 1];
        dp[0] = 1;
        for(int remaining = 0; remaining <= target; remaining++)
            for(int num : nums){
                if(remaining < num)
                    continue;
                dp[remaining] += dp[remaining - num];
            }
        return dp[target];
    }
}