class Solution {
    public int[] searchRange(int[] nums, int target) {
        int[] ans = new int[]{-1, -1};
        
        int end = this.bisectRight(nums, target) - 1;
        if(end == -1 || nums[end] != target){
            return ans;
        } else {
            ans[1] = end;
        }
        
        ans[0] = this.bisectLeft(nums, target);
        
        return ans;
    }
    
    private int bisectLeft(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
    
    private int bisectRight(int[] nums, int target) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    }
}