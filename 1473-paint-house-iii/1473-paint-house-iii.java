class Solution {
    public int minCost(int[] houses, int[][] cost, int m, int n, int target) {
        int[][] prev = new int[target + 2][n + 1];
        int[][] curr = new int[target + 2][n + 1];
        for(int i = 0; i <= target + 1; i++)
            for(int j = 0; j <= n; j++){
                if(i == target)
                    prev[i][j] = 0;
                else
                    prev[i][j] = Integer.MAX_VALUE;
                curr[i][j] = Integer.MAX_VALUE;
            }
    
        for(int i = m - 1; i >= 0; i--){
            for(int nhs = target; nhs >= 0; nhs--){
                for(int pcolor = n; pcolor >= 0; pcolor--){
                    if(houses[i] != 0){
                        curr[nhs][pcolor] = prev[
                            pcolor != houses[i] ? nhs + 1 : nhs
                        ][houses[i]];
                        continue;
                    }
                    
                    for(int j = 0; j < n; j++){
                        int res = prev[
                            pcolor != j + 1 ? nhs + 1 : nhs
                        ][j + 1];
                        if(res != Integer.MAX_VALUE)
                            curr[nhs][pcolor] = Math.min(
                                curr[nhs][pcolor],
                                cost[i][j] + res
                            );
                    }
                }
            }
            prev = curr;
            curr = new int[target + 2][n + 1];
            for(int k = 0; k <= target + 1; k++)
                for(int l = 0; l <= n; l++){
                    curr[k][l] = Integer.MAX_VALUE;
                }
            }
        return prev[0][0] == Integer.MAX_VALUE ? -1 : prev[0][0];
    }
}