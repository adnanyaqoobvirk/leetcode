class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        SortedSet<Integer> window = new TreeSet<>();
        HashMap<Integer, Integer> counts = new HashMap<>();
        int[] ans = new int[nums.length - k + 1];
        
        for(int i = 0; i < k; i++){
            Integer count = counts.get(nums[i]);
            if(count == null){
                counts.put(nums[i], 1);
                window.add(nums[i]);
            } else
                counts.put(nums[i], count + 1);
        }

        ans[0] = window.last();
        for(int i = k; i < nums.length; i++){
            Integer count = counts.get(nums[i - k]);
            if(count == 1){
                counts.remove(nums[i - k]);
                window.remove(nums[i - k]);
            } else
                counts.put(nums[i - k], count - 1);
            
            count = counts.get(nums[i]);
            if(count == null){
                counts.put(nums[i], 1);
                window.add(nums[i]);
            } else
                counts.put(nums[i], count + 1);
            ans[i - k + 1] = window.last();
        }
        
        return ans;
    }
}