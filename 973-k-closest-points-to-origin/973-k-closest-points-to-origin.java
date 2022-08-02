class Solution {
    public int[][] kClosest(int[][] points, int k) {
        int[][] distances = new int[points.length][2]; 
        for(int i = 0; i < points.length; ++i){
            distances[i][0] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            distances[i][1] = i;
        }
        
        Comparator<int[]> comparator = (d1, d2) -> Integer.compare(d1[0], d2[0]);
        Arrays.sort(
            distances, 
            comparator.thenComparing(
             (d1, d2) -> Integer.compare(d1[1], d2[1])
            )
        );
        
        int[][] ans = new int[k][];
        for(int i = 0; i < k; ++i){
            ans[i] = points[distances[i][1]];
        }
        return ans;
    }
}