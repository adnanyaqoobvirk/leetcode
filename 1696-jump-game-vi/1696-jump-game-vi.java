class Solution {
    public int maxResult(int[] nums, int k) {
        LinkedList<Pair<Integer,Integer>> q = new LinkedList<>();
        int ans = nums[nums.length - 1];
        
        q.add(new Pair(ans, nums.length - 1));
        for(int i = nums.length - 2; i >= 0; i--){
            while(q.size() > 0 && q.getFirst().getValue() > i + k)
                q.removeFirst();
            
            ans = nums[i] + q.getFirst().getKey();
            
            while(q.size() > 0 && q.getLast().getKey() < ans)
                q.removeLast();
            q.add(new Pair(ans, i));
        }
        
        return ans;
    }
}