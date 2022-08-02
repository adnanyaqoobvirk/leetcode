class Solution {
    public List<Boolean> checkArithmeticSubarrays(int[] nums, int[] l, int[] r) {
        int m = l.length, n = nums.length;
        
        List<Boolean> ans = new ArrayList<>();
        for(int i = 0; i < m; ++i){
            int sl = r[i] - l[i] + 1;
            if(sl == 1){
                ans.add(false);
            } else if(sl == 2){
                ans.add(true);
            } else {
                int[] ss = new int[sl];
                for(int j = 0; j < sl; ++j){
                    ss[j] = nums[j + l[i]];
                }
                Arrays.sort(ss);
                
                int diff = ss[1] - ss[0];
                int j = 2;
                for(; j < sl; ++j){
                    if(diff != ss[j] - ss[j - 1]){
                        ans.add(false);
                        break;
                    }
                }
                
                if(j == sl){
                    ans.add(true);
                }
            }
        }
        return ans;
    }
}