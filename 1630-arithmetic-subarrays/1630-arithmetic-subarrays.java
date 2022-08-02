class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        List<Boolean> ans = new ArrayList<>();
        for(int i = 0; i < l.length; ++i){
            int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
            for(int j = l[i]; j <= r[i]; ++j){
                min = Math.min(min, nums[j]);
                max = Math.max(max, nums[j]);
            }
            
            int size = r[i] - l[i];
            if((max - min) % size != 0){
                ans.add(false);
            } else {
                int diff = (max - min) / size;
                if(diff == 0){
                    ans.add(true);
                } else {
                    Set<Integer> seen = new HashSet<>();
                    int j = l[i];
                    for(; j <= r[i]; ++j){
                        if((nums[j] - min) % diff != 0 || seen.contains(nums[j])){
                            ans.add(false);
                            break;
                        }
                        seen.add(nums[j]);
                    }
                    
                    if(j > r[i]){
                        ans.add(true);
                    }
                }
            }
        }
        return ans;
    }
}