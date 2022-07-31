class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        int carry = k;
        for(int i = num.length - 1; i >= 0; i--){
            int sum = num[i] + carry;
            num[i] = sum % 10;
            carry = sum / 10;
        }
        
        List<Integer> ans = new ArrayList<>();
        while(carry > 0){
            ans.add(carry % 10);
            carry /= 10;
        }
        Collections.reverse(ans);
    
        for(int i = 0; i < num.length; i++){
            ans.add(num[i]);
        }
        return ans;
    }
}