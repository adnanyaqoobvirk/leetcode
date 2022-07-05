class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = new HashSet<>();
        for(int num : nums)
            numSet.add(num);
        
        int ans = 0;
        for(int num : nums){
            int count = 0;
            int nnum = num;
            while(numSet.contains(nnum)){
                numSet.remove(nnum);
                nnum--;
                count++;
            }
            
            nnum = num + 1;
            while(numSet.contains(nnum)){
                numSet.remove(nnum);
                nnum++;
                count++;
            }
            ans = Math.max(ans, count);
        }
        return ans;
    }
}