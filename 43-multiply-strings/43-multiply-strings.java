class Solution {
    public String multiply(String num1, String num2) {
        if(num1.equals("0") || num2.equals("0")){
            return "0";
        }
        
        if(num1.length() < num2.length()){
            String tmp = num1;
            num1 = num2;
            num2 = tmp;
        }
        
        int k = num1.length() + num2.length();
        int[] ans = new int[k];
        for(int j = num2.length() - 1; j >= 0; j--){
            k--;
            int d = num2.charAt(j) - '0';
            int carry = 0;
            int a = 0;
            for(int i = num1.length() - 1; i >= 0; i--){
                int p = (num1.charAt(i) - '0') * d + carry + ans[k - a];
                ans[k - a] = p % 10;
                carry = p / 10;
                a++;
            }
            while(carry > 0){
                int sum = ans[k - a] + carry;
                ans[k - a] = sum % 10;
                carry = sum / 10;
                a++;
            }
        }
        
        StringBuilder sb = new StringBuilder();
        boolean leading = true;
        for(int i = 0; i < ans.length; i++){
            if(!leading || ans[i] > 0){
                leading = false;
                sb.append((char) (ans[i] + 48));
            }
        }
        return sb.toString();
    }
}