class NumArray {
    private int n;
    private int[] tree;
    
    public NumArray(int[] nums) {
        this.n = nums.length;
        this.tree = new int[nums.length * 4];
        
        buildTree(tree, nums, 0, 0, this.n - 1);
    }
    
    public void update(int index, int val) {
        this.updateTree(0, index, val, 0, this.n - 1);
    }
    
    public int sumRange(int left, int right) {
        return searchTree(0, 0, this.n - 1, left, right);
    }
    
    private void buildTree(int[] tree, int[] nums, int tindex, int lo, int hi){
        if(lo == hi){
            tree[tindex] = nums[lo];
            return;
        }
        
        int mid = lo + (hi - lo) / 2;
        buildTree(tree, nums, 2 * tindex + 1, lo, mid);
        buildTree(tree, nums, 2 * tindex + 2, mid + 1, hi);
        
        tree[tindex] = tree[2 * tindex + 1] + tree[2 * tindex + 2];
    }
    
    private int searchTree(int tindex, int lo, int hi, int left, int right){
        if(right < lo || left > hi){
            return 0;
        }
        
        if(left <= lo && right >= hi){
            return this.tree[tindex];
        }
        
        int mid = lo + (hi - lo) / 2;
        
        if(right <= mid){
            return this.searchTree(tindex * 2 + 1, lo, mid, left, right);
        } else if(left > mid){
            return this.searchTree(tindex * 2 + 2, mid + 1, hi, left, right);
        } else {
            int l = this.searchTree(tindex * 2 + 1, lo, mid, left, right);
            int r = this.searchTree(tindex * 2 + 2, mid + 1, hi, left, right);
            
            return l + r;
        }
    }
    
    private void updateTree(int tindex, int index, int val, int lo, int hi){
        if(lo == hi){
            this.tree[tindex] = val;
            return;
        }
        
        int mid = lo + (hi - lo) / 2;
        
        if(index <= mid){
            this.updateTree(tindex * 2 + 1, index, val, lo, mid);
        } else if(index > mid){
            this.updateTree(tindex * 2 + 2, index, val, mid + 1, hi);
        }
        
        this.tree[tindex] = this.tree[tindex * 2 + 1] + this.tree[tindex * 2 + 2];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */