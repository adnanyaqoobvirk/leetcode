class Solution {
    public int minCost(int[][] costs) {
        int[] prev = new int[3], curr = new int[3];
        for(int i = costs.length - 1; i >= 0; i--){
            curr[0] = Math.min(costs[i][1] + prev[1], costs[i][2] + prev[2]);
            curr[1] = Math.min(costs[i][0] + prev[0], costs[i][2] + prev[2]);
            curr[2] = Math.min(costs[i][0] + prev[0], costs[i][1] + prev[1]);
            
            int[] tmp = prev;
            prev = curr;
            curr = tmp;
        }
        return Math.min(Math.min(prev[0], prev[1]), prev[2]);
    }
}