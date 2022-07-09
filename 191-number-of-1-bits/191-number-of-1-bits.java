public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int ans = 0;
        
        if(n < 0){
            ans += 1;
            n &= 0x7FFFFFFF;            
        }

        while(n > 0){
            n &= n - 1;
            ans += 1;
        }
        
        return ans;
    }
}