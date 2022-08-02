class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        if(k == n * n){
            return matrix[n - 1][n - 1];
        }
        
        PriorityQueue<Integer> heap = new PriorityQueue<>(
            (Integer o1, Integer o2) -> -Integer.compare(o1, o2)
        );
        for(int i = 0; i < n; ++i){
            for(int j = 0; j < n; ++j){
                heap.add(matrix[i][j]);
                if(heap.size() > k){
                    heap.remove();
                }
            }
        }
        return heap.peek();
    }
}