class Solution {
    public int nearestValidPoint(int x, int y, int[][] points) {
        int smallest_distance = Integer.MAX_VALUE, smallest_idx = -1;
        for(int i = 0; i < points.length; i++){
            int[] point = points[i];
            if(point[0] != x && point[1] != y)
                continue;
            
            int distance = Math.abs(point[0] - x) + Math.abs(point[1] - y);
            if(distance < smallest_distance){
                smallest_distance = distance;
                smallest_idx = i;
            }
        }
        return smallest_idx;
    }
}