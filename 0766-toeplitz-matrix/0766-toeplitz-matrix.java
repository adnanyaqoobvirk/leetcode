class Solution {
    public boolean isToeplitzMatrix(int[][] matrix) {
        for(int i = 0; i < matrix.length; i++){
            for(int j = 0; j < matrix[0].length; j++){
                int x = i - 1, y = j - 1;
                if(0 <= x && x < matrix.length && 0 <= y && y < matrix[0].length){
                    if(matrix[x][y] != matrix[i][j]){
                        return false;
                    }
                }
            }
        }
        return true;
    }
}