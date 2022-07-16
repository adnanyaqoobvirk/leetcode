class Solution {
    public int strStr(String haystack, String needle) {
        int m = haystack.length(), n = needle.length();
        
        if(n > m){
            return -1;
        }
        
        for(int i = 0; i < m; i++){
            boolean brokeEarly = false;
            for(int j = 0; j < n; j++){
                if(i + j < m && needle.charAt(j) == haystack.charAt(i + j)){
                    continue;
                } else {
                    brokeEarly = true;
                    break;
                }
            }
            if(!brokeEarly){
                return i;
            }
        }
        
        return -1;
    }
}