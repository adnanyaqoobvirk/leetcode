class Solution {
    public int shortestSequence(int[] rolls, int k) {
        Set<Integer> seen = new HashSet<>();
        int ans = 1;
        for(int roll : rolls){
            seen.add(roll);
            
            if(seen.size() == k){
                seen.clear();
                ans += 1;
            }
        }
        return ans;
    }
}