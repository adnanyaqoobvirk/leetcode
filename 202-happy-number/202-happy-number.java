class Solution {
    public boolean isHappy(int n) {
        int slow = n, fast = this.nxt(this.nxt(n));
        while(slow != fast && slow != 1){
            slow = this.nxt(slow);
            fast = this.nxt(this.nxt(fast));
        }
        return slow == 1 ? true : false;
    }
    
    private int nxt(int m){
        int n = 0;
        while(m > 0){
            int d = m % 10;
            n += d * d;
            m /= 10;
        }
        return n;
    }
}