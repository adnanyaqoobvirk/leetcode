class Solution {
    public int longestPalindrome(String s) {
        Map<Character, Integer> counts = new HashMap<>();
        for(char c : s.toCharArray()){
            if(!counts.containsKey(c)){
                counts.put(c, 0);
            }
            
            counts.put(c, counts.get(c) + 1);
        }
        
        int ans = 0;
        boolean oddExists = false;
        for(int cnt : counts.values()){
            if(cnt % 2 == 1){
                cnt -= 1;
                oddExists = true;
            }
            
            ans += cnt;
        }
        
        return oddExists ? ans + 1 : ans;
    }
}