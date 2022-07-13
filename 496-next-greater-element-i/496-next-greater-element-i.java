class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        Stack<Integer> stack = new Stack<>();
        Map<Integer, Integer> nextGreater = new HashMap<>();
        for(int i = 0; i < nums2.length; i++){
            while(stack.size() > 0 && stack.peek() < nums2[i]){
                nextGreater.put(stack.pop(), nums2[i]);
            }
            stack.push(nums2[i]);
        }
        
        int[] ans = new int[nums1.length];
        for(int i = 0; i < nums1.length; i++){
            int greater = nextGreater.getOrDefault(nums1[i], -1);
            ans[i] = greater;
        }
        return ans;
    }
}