class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int[] ans = new int[temperatures.length];
        Stack<Integer> stack = new Stack<>();
        for(int i = temperatures.length - 1; i >= 0; i--){
            while(stack.size() > 0 && temperatures[stack.peek()] <= temperatures[i]){
                stack.pop();
            }
            
            if(stack.size() != 0){
                ans[i] = stack.peek() - i;
            }
            stack.add(i);
        }
        return ans;
    }
}