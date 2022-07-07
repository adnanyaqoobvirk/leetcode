class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        if(s1.length() + s2.length() != s3.length())
            return false;
        
        boolean[] prev = new boolean[s2.length() + 1];
        boolean[] curr = new boolean[s2.length() + 1];
        for(int i = s1.length(); i >= 0; i--){
            for(int j = s2.length(); j >= 0; j--){
                int k = i + j;
                
                if(k == s3.length()){
                    curr[j] = true;
                    continue;
                }
                
                curr[j] = false;
                if(i < s1.length() && s1.charAt(i) == s3.charAt(k))
                    curr[j] = prev[j];
                
                if(j < s2.length() && s2.charAt(j) == s3.charAt(k))
                    curr[j] = curr[j] || curr[j + 1];
            }
            boolean[] tmp = prev;
            prev = curr;
            curr = tmp;
        }
        return prev[0];
    }
}