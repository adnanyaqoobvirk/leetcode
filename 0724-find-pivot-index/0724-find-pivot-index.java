class Solution {
    public int pivotIndex(int[] nums) {
        int[] prefixes = new int[nums.length];
        int prefix = 0;
        for(int i = nums.length - 1; i >= 0; --i){
            prefixes[i] = prefix;
            prefix += nums[i];
        }
        
        prefix = 0;
        for(int i = 0; i < nums.length; ++i){
            if(prefix == prefixes[i]){
                return i;
            }
            prefix += nums[i];
        }
        
        return -1;
    }
}