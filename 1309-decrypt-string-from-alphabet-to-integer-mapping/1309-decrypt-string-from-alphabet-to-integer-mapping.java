class Solution {
    public String freqAlphabets(String s) {
        StringBuilder sb = new StringBuilder();
        
        int j = 0;
        for(int i = 2; i < s.length(); i++){
            if(s.charAt(i) == '#'){
                sb.append((char) ((s.charAt(i - 2) - '0') * 10 + s.charAt(i - 1) - '0' + 96));
                j = i + 1;
            } else if (i - j >= 2){
                sb.append((char) (s.charAt(j) - '0' + 96));
                j++;
            }
        }
        
        for(; j < s.length(); j++){
            sb.append((char) (s.charAt(j) - '0' + 96));
        }
        
        return sb.toString();
    }
}