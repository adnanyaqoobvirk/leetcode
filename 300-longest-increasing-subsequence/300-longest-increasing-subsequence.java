class Solution {
    public int lengthOfLIS(int[] nums) {
        int[] prev = new int[nums.length + 1];
        int[] curr = new int[nums.length + 1];
        for(int pos = nums.length - 1; pos >= 0; pos--){
            for(int ppos = pos; ppos >= 0; ppos--){
                curr[ppos] = Math.max(
                    (nums[pos] > nums[ppos] ? 1 : 0) + prev[
                        nums[pos] > nums[ppos] ? pos : ppos
                    ],
                    prev[ppos]
                );
            }
            curr[nums.length] = Math.max(
                1 + prev[pos],
                prev[nums.length]
            );
            int[] tmp = curr;
            curr = prev;
            prev = tmp;
        }
        return prev[nums.length];
    }
}