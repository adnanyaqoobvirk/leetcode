class Solution {
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length, n = mat[0].length;
        if(r * c != m * n)
            return mat;
        
        int[][] ans = new int[r][c];
        int i = 0, j = 0;
        for(int[] row : mat){
            for (int col : row){
                ans[i][j] = col;
                j++;
                
                if(j == c){
                    j = 0;
                    i++;
                }
            }
        }
        return ans;
    }
}