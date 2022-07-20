class Solution {
    public int numMatchingSubseq(String s, String[] words) {
        Map<Character, List<Integer>> buckets = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            if(!buckets.containsKey(s.charAt(i)))
                buckets.put(s.charAt(i), new ArrayList<>());
            buckets.get(s.charAt(i)).add(i);
        }
        
        int ans = 0;
        for(String word : words){
            int i = 0, j = 0;
            for(; j < word.length(); j++){
                if(!buckets.containsKey(word.charAt(j))){
                    break;
                }
                
                List<Integer> b = buckets.get(word.charAt(j));
                int lo = 0, hi = b.size();
                while(lo < hi){
                    int mid = lo + (hi - lo) / 2;
                    if(b.get(mid) >= i){
                        hi = mid;
                    } else{
                        lo = mid + 1;
                    }
                }
                if(lo == b.size()){
                    break;
                }
                i = b.get(lo) + 1;
            }
            if(j == word.length()){
                ans++;
            }
        }
        
        return ans;
    }
}