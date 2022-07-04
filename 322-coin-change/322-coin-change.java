class Solution {
    public int coinChange(int[] coins, int amount) {
        Queue<Integer> q = new LinkedList<>();
        q.add(amount);
        
        HashSet<Integer> seen = new HashSet<>();
        seen.add(amount);
        
        int ans = 0;
        while (q.size() > 0){
            int n = q.size();
            for (int i = 0; i < n; i++){
                int r = q.poll();
                
                if (r == 0)
                    return ans;
                
                if (r > 0)
                    for (int coin : coins){
                        if (seen.contains(r - coin))
                            continue;
                        q.add(r - coin);
                        seen.add(r - coin);
                    }
            }
            ans += 1;
        }
        
        return -1; 
    }
}