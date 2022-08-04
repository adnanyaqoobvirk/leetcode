class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> groups = new HashMap<>();
        for(String s : strs){
            char[] sChars = s.toCharArray();
            Arrays.sort(sChars);
            String sortedS = new String(sChars);
            if(!groups.containsKey(sortedS)){
                groups.put(sortedS, new ArrayList<>());
            }
            groups.get(sortedS).add(s);
        }
        
        return new ArrayList(groups.values());
    }
}