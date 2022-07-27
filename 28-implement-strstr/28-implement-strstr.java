class Solution {
    public int strStr(String haystack, String needle) {
        int n = haystack.length(), m = needle.length();
        if(m > n){
            return -1;
        }
        
        int[] lps = new int[m];
        int i = 0, j = 1;
        while(j < m){
            if(needle.charAt(i) == needle.charAt(j)){
                i++;
                lps[j] = i;
                j++;
            } else {
                if(i == 0){
                    j++;
                } else {
                    i = lps[i - 1];
                }
            }
        }
        
        i = j = 0;
        while(i < n){
            if(haystack.charAt(i) == needle.charAt(j)){
                i++;
                j++;
            } else {
                if(j == 0){
                    i++;
                } else {
                    j = lps[j - 1];
                }
            }
            
            if(j == m){
                return i - m;
            }
        }
        
        return -1;
    }
}