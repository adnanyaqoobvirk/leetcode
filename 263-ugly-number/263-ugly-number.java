class Solution {
    public boolean isUgly(int n) {
        if(n <= 0){
            return false;
        }
        
        if(n == 1){
            return true;
        }
        
        for(int f : new int[]{2, 3, 5}){
            if((n % f) == 0 && this.isUgly(n / f)){
                return true;
            }
        }
        
        return false;
    }
}