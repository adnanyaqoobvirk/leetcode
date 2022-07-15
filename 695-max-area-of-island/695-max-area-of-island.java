class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int[] dx = new int[]{-1, 0, 1, 0};
        int[] dy = new int[]{0, 1, 0, -1};
        int maxArea = 0;
        for(int i = 0; i < grid.length; i++)
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == 0)
                    continue;
                
                ArrayList<int[]> q = new ArrayList<>();
                q.add(new int[]{i, j});
                int area = 1;
                grid[i][j] = 0;
                
                while(q.size() > 0){
                    ArrayList<int[]> nq = new ArrayList<>();
                    for(int[] pair : q){
                        for(int k = 0; k < 4; k++){
                            int ni = pair[0] + dx[k];
                            int nj = pair[1] + dy[k];
                            if(
                                0 <= ni && ni < grid.length && 
                                0 <= nj && nj < grid[0].length && 
                                grid[ni][nj] == 1
                            ){
                                grid[ni][nj] = 0;
                                nq.add(new int[]{ni, nj});
                            }
                        }
                    }
                    q = nq;
                    area += q.size();
                    maxArea = Math.max(maxArea, area);
                }
            }
        return maxArea;
    }
}