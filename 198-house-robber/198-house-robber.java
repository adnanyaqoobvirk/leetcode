class Solution {
    public int rob(int[] nums) {
        int prev = 0, curr = 0;
        for(int i = nums.length - 1; i >= 0; i--){
            int tmp = prev;
            prev = curr;
            curr = Math.max(nums[i] + tmp, curr);
        }
        return curr;
    }
}