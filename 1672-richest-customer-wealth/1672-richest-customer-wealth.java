class Solution {
    public int maximumWealth(int[][] accounts) {
        int max = 0;
        for(int[] account : accounts){
            int total = 0;
            for(int money : account){
                total += money;
            }
            max = Math.max(max, total);
        }
        return max;
    }
}