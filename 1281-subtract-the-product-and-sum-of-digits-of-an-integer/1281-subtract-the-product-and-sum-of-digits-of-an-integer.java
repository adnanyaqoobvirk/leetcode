class Solution {
    public int subtractProductAndSum(int n) {
        long product = 1;
        int total = 0;
        while(n > 0){
            int d = n % 10;
            n /= 10;
            
            product *= d;
            total += d;
        }
        return (int) product - total;
    }
}