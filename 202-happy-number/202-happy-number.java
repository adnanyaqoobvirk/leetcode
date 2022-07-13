class Solution {
    public boolean isHappy(int n) {
        Set<Integer> seen = new HashSet<>();
        while(n > 1){
            if(seen.contains(n))
                return false;
            seen.add(n);
            
            int total = 0;
            while(n > 0){
                int d = n % 10;
                total += d * d;
                n /= 10;
            }
            n = total;
        }
        return true;
    }
}