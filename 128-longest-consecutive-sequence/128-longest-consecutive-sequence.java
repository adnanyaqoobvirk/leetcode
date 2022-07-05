class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        for(int num : nums)
            numSet.add(num);
        
        int ans = 0;
        for(int num : nums){
            if(!numSet.contains(num - 1)){
                int count = 0;
                while(numSet.contains(num)){
                    num++;
                    count++;
                }
                ans = Math.max(ans, count);
            }
        }
        return ans;
    }
}