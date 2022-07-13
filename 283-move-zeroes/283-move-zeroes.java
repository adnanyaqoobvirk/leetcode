class Solution {
    public void moveZeroes(int[] nums) {
        int left = 0, right = 0;
        while(right < nums.length){
            if(nums[left] != 0){
                left++;
            } else if(nums[right] != 0){
                nums[left] = nums[right];
                nums[right] = 0;
                left++;
            }
            right++;
        }
    }
}