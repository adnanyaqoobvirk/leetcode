class Solution {
    public boolean areAlmostEqual(String s1, String s2) {
        int prev = -1, swaps = 0;
        for(int i = 0; i < s1.length(); i++){
            if(s1.charAt(i) != s2.charAt(i)){
                if(prev != -1 && (
                    s1.charAt(prev) != s2.charAt(i) || 
                    s2.charAt(prev) != s1.charAt(i)
                    )
                  )
                    return false;
                prev = i;
                swaps++;
            }
        }
        return swaps == 2 || swaps == 0 ? true : false;
    }
}