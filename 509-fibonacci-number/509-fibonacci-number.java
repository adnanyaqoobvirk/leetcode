class Solution {
    public int fib(int n) {
        int prev = 0, curr = 1;
        for(int i = 0; i < n; i++){
            int tmp = curr + prev;
            prev = curr;
            curr = tmp;
        }
        return prev;
    }
}