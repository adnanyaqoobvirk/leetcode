import java.text.StringCharacterIterator;

class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        Map<Character, List<StringCharacterIterator>> buckets = new HashMap<>();
        for(String word : words){
            if(!buckets.containsKey(word.charAt(0)))
                buckets.put(word.charAt(0), new ArrayList<>());
            buckets.get(word.charAt(0)).add(new StringCharacterIterator(word));
        }
        
        int ans = 0;
        for(char c : s.toCharArray()){
            List<StringCharacterIterator> b = buckets.get(c);
            if(b != null){
                buckets.put(c, new ArrayList<>());
                
                for(StringCharacterIterator itr : b){
                    char nc = itr.next();
                    if(nc == itr.DONE){
                        ans++;
                    } else{
                        if(!buckets.containsKey(nc))
                            buckets.put(nc, new ArrayList<>());
                        buckets.get(nc).add(itr);
                    }
                }
            }
        }
        return ans;
    }
}