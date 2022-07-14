class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        Map<Character, Integer> charMap = new HashMap<>();
        for(int i = 0; i < order.length(); i++)
            charMap.put(order.charAt(i), i);
        
        for(int i = 1; i < words.length; i++){
            boolean exitEarly = false;
            for(int j = 0; j < Math.min(words[i].length(), words[i - 1].length()); j++){
                if(words[i].charAt(j) == words[i - 1].charAt(j))
                    continue;
                
                if(charMap.get(words[i].charAt(j)) < charMap.get(words[i - 1].charAt(j)))
                    return false;
                else
                    exitEarly = true;
                    break;
            }
            if(!exitEarly && words[i].length() < words[i - 1].length())
                return false;
        }
        
        return true;
    }
}