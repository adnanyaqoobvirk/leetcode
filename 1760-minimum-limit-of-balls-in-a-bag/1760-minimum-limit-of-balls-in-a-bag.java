class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int maxNum = 0;
        for(int num : nums)
            maxNum = Math.max(maxNum, num);
        
        int lo = 1, hi = maxNum;
        while(lo < hi){
            int mid = lo + (hi - lo) / 2;
            
            int ops = 0;
            for(int num : nums)
                ops += (num - 1) / mid;
            
            if(ops > maxOperations)
                lo = mid + 1;
            else
                hi = mid;
        }
        return lo;
    }
}