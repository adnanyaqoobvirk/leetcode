class Solution {
    public int numSquares(int n) {
        int m = (int) Math.sqrt(n) + 1;
        int[] squares = new int[m];
        for(int num = 1; num < m; num++)
            squares[num - 1] = num * num;
        
        HashSet<Integer> q = new HashSet<>();
        q.add(n);
        
        int ans = 0;
        while(q.size() > 0){
            HashSet<Integer> nq = new HashSet<>();
            for(int remaining : q){
                if(remaining == 0)
                    return ans;
                
                int r = (int) Math.sqrt(remaining);
                for(int i = 0; i < r; i++){
                    int nr = remaining - squares[i];
                    if(!nq.contains(nr))
                        nq.add(nr);
                }
            }
            q = nq;
            ans++;
        }
        
        return ans;
    }
}