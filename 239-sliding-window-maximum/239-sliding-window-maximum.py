class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        LinkedList<Pair<Integer, Integer>> q = new LinkedList<>();
        int[] ans = new int[nums.length - k + 1];
        
        for(int i = 0; i < k; i++){
            while(q.size() > 0 && q.getLast().getKey() < nums[i])
                q.removeLast();
            q.add(new Pair(nums[i], i));
        }
        ans[0] = q.getFirst().getKey();
        
        for(int i = k; i < nums.length; i++){
            while(q.size() > 0 && q.getFirst().getValue() <= i - k)
                q.removeFirst();
            
            while(q.size() > 0 && q.getLast().getKey() < nums[i])
                q.removeLast();
            q.add(new Pair(nums[i], i));
            ans[i - k + 1] = q.getFirst().getKey();
        }
        
        return ans;
    }
}