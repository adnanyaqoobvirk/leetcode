class NumArray {
    private int[] nums;
    private int[] tree;
    
    public NumArray(int[] nums) {
        this.nums = nums;
        this.tree = new int[nums.length + 1];
        
        for(int i = 0; i < this.nums.length; i++){
            this.updateTree(i, this.nums[i]);
        }
    }
    
    public void update(int index, int val) {
        int diff = val - this.nums[index];
        this.nums[index] = val;
        this.updateTree(index, diff);
    }
    
    public int sumRange(int left, int right) {
        return this.getSum(right) - this.getSum(left - 1);
    }
    
    private int getSum(int index){
        int sum = 0;
        index += 1;
        while(index > 0){
            sum += this.tree[index];
            index -= index & -index;
        }
        return sum;
    }
    
    private void updateTree(int index, int val){
        index += 1;
        while(index < this.tree.length){
            this.tree[index] += val;
            index += index & -index;
        }
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * obj.update(index,val);
 * int param_2 = obj.sumRange(left,right);
 */