class Solution {
    public int maxSubArray(int[] nums) {
        int currPicked = 0, currNotPicked = Integer.MIN_VALUE;
        for(int i = nums.length - 1; i >= 0; i--){
            int prevPicked = currPicked;
            currPicked = Math.max(
                nums[i] + prevPicked,
                0
            );
            currNotPicked = Math.max(
                nums[i] + prevPicked,
                currNotPicked
            );
        }
        return currNotPicked;
    }
}