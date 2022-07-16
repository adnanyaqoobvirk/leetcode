class Solution {
    public boolean isMonotonic(int[] nums) {
        int incr = 0;
        for(int i = 1; i < nums.length; i++){
            if(nums[i] > nums[i - 1]){
                if(incr == 0)
                    incr = 1;
                else if (incr != 1)
                    return false;  
            } else if (nums[i] < nums[i - 1]) {
                if(incr == 0)
                    incr = -1;
                else if (incr != -1)
                    return false;   
            }
        }
        return true;
    }
}