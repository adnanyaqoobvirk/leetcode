class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] ans = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(ans, (n1, n2) -> {
            Integer n1Ones = Integer.bitCount(n1), n2Ones = Integer.bitCount(n2);
            if(n1Ones == n2Ones)
                return n1 - n2;
            else
                return n1Ones - n2Ones;
        });
        return Arrays.stream(ans).mapToInt(Integer::intValue).toArray();
        
    }
}