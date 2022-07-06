class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int lo = 0, hi = nums.length;
        while(lo < hi){
            int mid = lo + (hi - lo) / 2;
            if(isSumEqualGreater(nums, target, mid + 1))
                hi = mid;
            else
                lo = mid + 1;
        }
        return lo == nums.length ? 0 : lo + 1;
    }
    
    private boolean isSumEqualGreater(int[] nums, int target, int l){
        int total = 0;
        for(int i = 0; i < l; i++)
            total += nums[i];
        
        for(int j = l; j < nums.length; j++){
            if (total >= target)
                return true;
            total -= nums[j - l];
            total += nums[j];
        }
        return total >= target;
    }
}