class Solution {
    public boolean repeatedSubstringPattern(String s){
        StringBuilder sb = new StringBuilder();
        for(int i = 1; i < s.length(); i++){
            sb.append(s.charAt(i));
        }
        
        for(int i = 0; i < s.length() - 1; i++){
            sb.append(s.charAt(i));
        }
        
        return sb.toString().contains(s);
    }
}