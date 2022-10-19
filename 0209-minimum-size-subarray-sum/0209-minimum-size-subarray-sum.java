class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int minLen = Integer.MAX_VALUE;
        int total = 0, left = 0, right = 0;
        while(right < nums.length){
            total += nums[right];
            right++;
            while(left <= right && total >= target){
                minLen = Math.min(minLen, right - left);
                total -= nums[left];
                left += 1;
            }
        }
        return minLen == Integer.MAX_VALUE ? 0 : minLen;
    }
}