class Solution {
    public int minimumSum(int num) {
        int digits[] = new int[4];
        for(int i = 0; i < 4; i++){
            digits[i] = num % 10;
            num /= 10;
        }
        Arrays.sort(digits);
        
        int num1 = 0, num2 = 0;
        for(int i = 0; i < 4; i++){
            if ((i & 1) == 1)
                num1 = num1 * 10 + digits[i];
            else
                num2 = num2 * 10 + digits[i];
        }
        
        return num1 + num2;
    }
}