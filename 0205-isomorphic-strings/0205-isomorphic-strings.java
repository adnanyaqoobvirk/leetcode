class Solution {
    public boolean isIsomorphic(String s, String t) {
        Map<Character, Character> map = new HashMap<>();
        Set<Character> mapped = new HashSet<>();
        for(int i = 0; i < s.length(); i++){
            if(!map.containsKey(s.charAt(i))){
                if(mapped.contains(t.charAt(i))){
                    return false;
                }
                map.put(s.charAt(i), t.charAt(i));
                mapped.add(t.charAt(i));
            }
            if(map.get(s.charAt(i)) != t.charAt(i)){
                return false;
            }
        }
        return true;
    }
}