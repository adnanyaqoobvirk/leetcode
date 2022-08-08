class Solution {
    public int addDigits(int num) {
        while(num > 9){
            int n = num;
            int total = 0;
            while(n > 0){
                total += n % 10;
                n /= 10;
            }
            num = total;
        }
        return num;
    }
}