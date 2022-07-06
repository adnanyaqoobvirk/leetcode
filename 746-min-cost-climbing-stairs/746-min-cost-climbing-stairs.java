class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int prev = Integer.MAX_VALUE, curr = 0;
        for(int i = cost.length - 1; i >= 0; i--){
            int tmp = cost[i] + Math.min(prev, curr);
            prev = curr;
            curr = tmp;
        }
        return Math.min(prev, curr);
    }
}