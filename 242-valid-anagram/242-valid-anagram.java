class Solution {
    public boolean isAnagram(String s, String t) {
        int[] charCounts = new int[26];
        for(char c : s.toCharArray())
            charCounts[c - 'a'] += 1;
        
        for(char c : t.toCharArray())
            charCounts[c - 'a'] -= 1;
        
        for(int i = 0; i < 26; i++)
            if(charCounts[i] != 0)
                return false;
        return true;
    }
}