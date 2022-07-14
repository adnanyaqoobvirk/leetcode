class Solution {
    public String toLowerCase(String s) {
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if(c <= 90 && c >= 65)
                sb.append((char) (c + 32));
            else
                sb.append(c);
        }
        return sb.toString();
    }
}