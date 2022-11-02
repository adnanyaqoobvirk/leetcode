class Solution {
    public int smallestCommonElement(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        Map<Integer, Integer> counts = new HashMap<>();
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int count = counts.getOrDefault(mat[i][j], 0) + 1;
                if(count == m){
                    return mat[i][j];
                }
                counts.put(mat[i][j], count);
            }
        }
        return -1;
    }
}