class Solution {
    public int[] sortByBits(int[] arr) {
        int MAX_BITS = 15;
        
        Arrays.sort(arr);
        
        Map<Integer, List<Integer>> bitBuckets = new HashMap<>();
        for(int i = 0; i < MAX_BITS; i++){
            bitBuckets.put(i, new ArrayList<Integer>());
        }
        
        for(int num : arr){
            int ones = 0, n = num;
            while(n > 0){
                n &= n - 1;
                ones++;
            }
            bitBuckets.get(ones).add(num);
        }
        
        int[] ans = new int[arr.length];
        int i = 0;
        for(int ones = 0; ones < MAX_BITS; ones++){
            for(int num : bitBuckets.get(ones)){
                ans[i++] = num;
            }
        }
        return ans;
        
    }
}