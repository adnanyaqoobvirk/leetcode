class Solution {
    public boolean canMakeArithmeticProgression(int[] arr) {
        Map<Integer, Integer> counts = new HashMap<>();
        int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
        for(int num : arr){
            counts.put(num, counts.getOrDefault(num, 0) + 1);
            min = Math.min(min, num);
            max = Math.max(max, num);
        }
        
        int diff = (max - min) / (arr.length - 1);
        
        if(diff == 0 && counts.size() == 1)
            return true;
        
        int curr = min + diff;
        while(curr <= max){
            Integer count = counts.get(curr);
            if(count == null || count > 1)
                return false;
            curr += diff;
        }
        return true;
    }
}