class Solution {
    public int lengthOfLIS(int[] nums) {
        ArrayList<Integer> maxLIS = new ArrayList<>();
        for(int i = 0; i < nums.length; i++){
            int lo = 0, hi = maxLIS.size();
            while(lo < hi){
                int mid = lo + (hi - lo) / 2;
                if(maxLIS.get(mid) >= nums[i])
                    hi = mid;
                else
                    lo = mid + 1;
            }
            if(lo == maxLIS.size())
                maxLIS.add(nums[i]);
            else
                maxLIS.set(lo, nums[i]);
        }
        return maxLIS.size();
    }
}