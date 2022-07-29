class Solution {
    public List<String> findAndReplacePattern(String[] words, String pattern) {
        List<String> ans = new ArrayList<>();
        for(String word : words){
            Map<Character, Character> pCharMap = new HashMap<>();
            Map<Character, Character> wCharMap = new HashMap<>();
            int i = 0;
            for(; i < pattern.length(); i++){
                if(pCharMap.getOrDefault(pattern.charAt(i), word.charAt(i)) != word.charAt(i)){
                    break;
                }
                
                if(wCharMap.getOrDefault(word.charAt(i), pattern.charAt(i)) != pattern.charAt(i)){
                    break;
                }
                
                pCharMap.put(pattern.charAt(i), word.charAt(i));
                wCharMap.put(word.charAt(i), pattern.charAt(i));
            }
            
            if(i == pattern.length()){
                ans.add(word);
            }
        }
        return ans;
    }
}