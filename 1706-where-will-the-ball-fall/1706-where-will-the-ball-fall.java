class Solution {
    public int[] findBall(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        
        int[] ans = new int[n];
        for(int col = 0; col < n; col++) {
            int r = 0, c = col;
            while(r < m){
                if(grid[r][c] == 1) {
                    if(c == n - 1 || grid[r][c + 1] == -1) {
                        ans[col] = -1;
                        break;
                    } else {
                        r++;
                        c++; 
                    }  
                } else {
                    if(c == 0 || grid[r][c - 1] == 1){
                        ans[col] = -1;
                        break;
                    } else {
                        r++;
                        c--; 
                    }  
                }
            }
            if(ans[col] != -1){
                ans[col] = c;
            }
        }
        return ans;
    }
}