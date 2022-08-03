class SeatManager {
    private PriorityQueue<Integer> heap;
    
    public SeatManager(int n) {
        this.heap = new PriorityQueue<Integer>();
        for(int i = 1; i <= n; ++i){
            heap.add(i);
        }
    }
    
    public int reserve() {
        return this.heap.remove();
    }
    
    public void unreserve(int seatNumber) {
        this.heap.add(seatNumber);
    }
}

/**
 * Your SeatManager object will be instantiated and called as such:
 * SeatManager obj = new SeatManager(n);
 * int param_1 = obj.reserve();
 * obj.unreserve(seatNumber);
 */