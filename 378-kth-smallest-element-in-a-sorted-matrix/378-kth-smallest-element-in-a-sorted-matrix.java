class Solution {
    public int kthSmallest(int[][] matrix, int k) {
        int n = matrix.length;
        int squareN = n * n;
        
        PriorityQueue<Integer> heap;
        
        if(k > squareN / 2){
            heap = new PriorityQueue<>();
            k = squareN - k + 1;
        } else {
            heap = new PriorityQueue<>(
                (Integer o1, Integer o2) -> -Integer.compare(o1, o2)
            );
        }
        
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