class Solution {
    public int change(int amount, int[] coins) {
        int[] prev = new int[amount + 1], curr = new int[amount + 1];
        prev[0] = curr[0] = 1;
        for(int pos = coins.length - 1; pos >= 0; pos--){
            for(int remaining = 0; remaining <= amount; remaining++){
                curr[remaining] = prev[remaining];
                if(remaining - coins[pos] >= 0)
                    curr[remaining] += curr[remaining - coins[pos]];
            }
            int[] tmp = prev;
            prev = curr;
            curr = tmp;
        }
        return prev[amount];
    }
}