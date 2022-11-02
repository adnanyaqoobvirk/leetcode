class Solution {
    public int smallestCommonElement(int[][] mat) {
        int m = mat.length, n = mat[0].length;
        Map<Integer, Integer> counts = new HashMap<>();
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                counts.put(mat[i][j], counts.getOrDefault(mat[i][j], 0) + 1);
                if(counts.get(mat[i][j]) == m){
                    return mat[i][j];
                }
            }
        }
        return -1;
    }
}