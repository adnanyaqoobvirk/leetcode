class Solution {
    public int rob(int[] nums) {
        if(nums.length == 1)
            return nums[0];
            
        int[][] params = new int[][]{
            new int[]{0, nums.length - 1}, 
            new int[]{1, nums.length}
        };
        
        int ans = 0;
        for(int[] param : params){
            int start = param[0], m = param[1];
            int prev = 0, curr = 0;
            for(int i = m - 1; i >= start; i--){
                int tmp = prev;
                prev = curr;
                curr = Math.max(nums[i] + tmp, curr);
            }
            ans = Math.max(ans, curr);
        }
        return ans;
    }
}