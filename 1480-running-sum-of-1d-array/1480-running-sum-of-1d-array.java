class Solution {
    public int[] runningSum(int[] nums) {
        int total = 0;
        int[] ans = new int[nums.length];
        for(int i = 0; i < nums.length; ++i){
            total += nums[i];
            ans[i] = total;
        }
        return ans;
    }
}