class NumArray {
    int[] prefixArray;

    public NumArray(int[] nums) {
        this.prefixArray = new int[nums.length];
        this.prefixArray[0] = nums[0];
        for(int i = 1; i < nums.length; i++)
            this.prefixArray[i] = this.prefixArray[i - 1] + nums[i];
    }
    
    public int sumRange(int left, int right) {
        if(left == 0)
            return this.prefixArray[right];
        else
            return this.prefixArray[right] - this.prefixArray[left - 1];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */