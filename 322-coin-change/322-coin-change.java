class Solution {
    public int coinChange(int[] coins, int amount) {
        ArrayList<Integer> q = new ArrayList<>();
        q.add(amount);
        
        HashSet<Integer> seen = new HashSet<Integer>();
        seen.add(amount);
        
        int ans = 0;
        while (q.size() > 0){
            ArrayList<Integer> nq = new ArrayList<Integer>();
            
            for(Integer r : q){
                if (r == 0)
                    return ans;
                
                if (r > 0)
                    for (int coin : coins){
                        if (seen.contains(r - coin))
                            continue;
                        nq.add(r - coin);
                        seen.add(r - coin);
                    }
            }
            q = nq;
            ans += 1;
        }
        
        return -1; 
    }
}