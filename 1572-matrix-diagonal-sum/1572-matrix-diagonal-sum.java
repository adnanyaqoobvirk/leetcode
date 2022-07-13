class Solution {
    public int diagonalSum(int[][] mat) {
        int total = 0;
        for(int i = 0; i < mat.length; i++){
            total += mat[i][i] + mat[i][mat.length - i - 1];
        }
        if((mat.length & 1) == 1)
            return total - mat[mat.length / 2][mat.length / 2];
        else
            return total;
    }
}