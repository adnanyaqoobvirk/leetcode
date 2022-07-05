class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums.length <= 1)
            return nums.length;
            
        Arrays.sort(nums);
        
        int ans = 0, count = 1;
        for(int i = 1; i < nums.length; i++){
            int diff = nums[i] - nums[i - 1];
            if(diff == 1)
                count++;
            else if(diff == 0)
                continue;
            else{
                ans = Math.max(ans, count);
                count = 1;
            }
        }
        return Math.max(ans, count);
    }
}