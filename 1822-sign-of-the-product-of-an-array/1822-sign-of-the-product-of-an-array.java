class Solution {
    public int arraySign(int[] nums) {
        boolean neg = false;
        for(int num : nums){
            if(num == 0)
                return 0;
            
            if(num < 0)
                neg = !neg;
        }
        return neg ? -1 : 1;
    }
}