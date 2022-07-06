class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        
        int combs = 0;
        for(int i = 0; i < nums.length - 2; i++){
            int lo = i + 2;
            for(int j = i + 1; j < nums.length - 1; j++){
                int total = nums[i] + nums[j];
                
                int hi = nums.length;
                while(lo < hi){
                    int mid = lo + (hi - lo) / 2;
                    if(nums[mid] >= total)
                        hi = mid;
                    else
                        lo = mid + 1;
                }
                combs += Math.max(0, lo - j - 1);
            }
        }
        return combs;
    }
}