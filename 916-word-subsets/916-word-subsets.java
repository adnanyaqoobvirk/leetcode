class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] maxCharCount = new int[26];
        for(String word : words2){
            int[] charCount = new int[26];
            for(int i = 0; i < word.length(); i++){
                int j = word.charAt(i) - 'a';
                charCount[j]++;
                maxCharCount[j] = Math.max(maxCharCount[j], charCount[j]);
            }
        }
        
        List<String> ans = new ArrayList<>();
        for(String word : words1){
            int[] charCount = new int[26];
            int i = 0;
            for(; i < word.length(); i++){
                int j = word.charAt(i) - 'a';
                charCount[j]++;
            }
            
            for(i = 0; i < 26; i++){
                if(maxCharCount[i] > charCount[i]){
                    break;
                }
            }
            
            if(i != 26){
                continue;
            }
            
            ans.add(word);
        }
        
        return ans;
    }
}