class Solution {
    public static final int MAX_CHARS = 26;
    public static final int MOD = 900001;
    
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        if(n > m){
            return -1;
        }
        
        int h = 1;
        for(int i = 0; i < n - 1; i++){
            h = (MAX_CHARS * h) % MOD;
        }
        
        int nhash = 0, mhash = 0;
        for(int i = 0; i < n; i++){
            nhash = (MAX_CHARS * nhash + needle.charAt(i)) % MOD;
            mhash = (MAX_CHARS * mhash + haystack.charAt(i)) % MOD;
        }
        
        for(int i = n; i <= m; i++){
            int k = i - n;
            if(nhash == mhash){
                int j;
                for(j = 0; j < n; j++){
                    if(needle.charAt(j) != haystack.charAt(j + k)){
                        break;
                    }
                }
                if(j == n){
                    return k;
                }
            }
            
            if(i < m){
                mhash = (MAX_CHARS * (mhash - haystack.charAt(k) * h) + haystack.charAt(i)) % MOD;
                
                if(mhash < 0){
                    mhash = (MOD + mhash);
                }
            }
        }
        
        return -1;
    }
}