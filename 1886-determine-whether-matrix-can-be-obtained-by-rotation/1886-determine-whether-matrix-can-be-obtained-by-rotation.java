class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        for(int k = 0; k < 4; ++k){
            this.rotate(mat);
            
            int i = 0;
            for(; i < mat.length; ++i){
                int j = 0;
                for(; j < mat.length; ++j){
                    if(mat[i][j] != target[i][j]){
                        break;
                    }
                }
                
                if(j != mat.length){
                    break;
                }
            }
            
            if(i == mat.length){
                return true;
            }
        }
        
        return false;
    }
    
    private void rotate(int[][] mat){
        int n = mat.length;
        
        for(int i = 0; i < n; ++i){
            for(int j = i + 1; j < n; ++j){
                int tmp = mat[i][j];
                mat[i][j] = mat[j][i];
                mat[j][i] = tmp;
            }
        }
        
        for(int i = 0; i < n; ++i){
            int l = 0, r = n - 1;
            while(l < r){
                int tmp = mat[i][l];
                mat[i][l] = mat[i][r];
                mat[i][r] = tmp;
                ++l;
                --r;
            }
        }
    }
}