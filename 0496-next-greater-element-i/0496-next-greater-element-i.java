class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Map<Integer, Integer> ngMap = new HashMap<>();
        List<Integer> stack = new ArrayList<>();
        for(int i = nums2.length - 1; i >= 0; i--){
            while(stack.size() > 0 && stack.get(stack.size() - 1) <= nums2[i]){
                stack.remove(stack.size() - 1);
            }
            ngMap.put(nums2[i], stack.size() == 0 ? -1 : stack.get(stack.size() - 1));
            stack.add(nums2[i]);
        }
        
        int[] ans = new int[nums1.length];
        for(int i = 0; i < nums1.length; i++){
            ans[i] = ngMap.getOrDefault(nums1[i], -1);
        }
        return ans;
    }
}