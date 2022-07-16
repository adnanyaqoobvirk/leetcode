class Solution {
    public int strStr(String haystack, String needle) {
        int h = haystack.length(), n = needle.length();
        if(n > h){
            return -1;
        }
        
        long nhash = 0, hhash = 0;
        for(int i = 0; i < n; i++){
            nhash += needle.charAt(i) - 97;
            hhash += haystack.charAt(i) - 97;
        }
        
        for(int i = n; i <= h; i++){
            int k = i - n;
            if(nhash == hhash){
                boolean exitEarly = false;
                for(int j = 0; j < n; j++){
                    if(needle.charAt(j) != haystack.charAt(j + k)){
                        exitEarly = true;
                        break;
                    }
                }
                if(!exitEarly){
                    return k;
                }
            }
            
            if(i < h){
                hhash += haystack.charAt(i) - haystack.charAt(k);
            }
        }
        
        return -1;
    }
}