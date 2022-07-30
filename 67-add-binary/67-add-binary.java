class Solution {
    public String addBinary(String a, String b) {
        if(a.length() < b.length()){
            String t = a;
            a = b;
            b = t;
        }
        
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int j = b.length() - 1;
        for(int i = a.length() - 1; i >= 0; --i){
            int sum = a.charAt(i) - '0' + carry;
            if(j >= 0){
                sum += b.charAt(j) - '0';
                --j;
            }
            
            carry = sum / 2;
            sb.append((char) (sum % 2 + 48));
        }
        
        if(carry > 0){
            sb.append('1');
        }
        
        return sb.reverse().toString();
    }
}