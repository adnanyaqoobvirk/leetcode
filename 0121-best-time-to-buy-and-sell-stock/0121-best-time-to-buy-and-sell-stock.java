class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0, maxRight = 0;
        for(int i = prices.length - 1; i >= 0; i--){
            maxRight = Math.max(maxRight, prices[i]);
            maxProfit = Math.max(maxProfit, maxRight - prices[i]);
        }
        return maxProfit;
    }
}