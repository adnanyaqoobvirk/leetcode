class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Map<Integer, Integer> seen = new HashMap<>();
        seen.put(0, 0);
        
        int total = 0;
        int r;
        for(int i = 0; i < nums.length; i++){
            total += nums[i];
            r = total % k;
            if(!seen.containsKey(r)){
                seen.put(r, i + 1);
            } else if(seen.get(r) < i){
                return true;
            }
        }
        
        return false;
    }
}