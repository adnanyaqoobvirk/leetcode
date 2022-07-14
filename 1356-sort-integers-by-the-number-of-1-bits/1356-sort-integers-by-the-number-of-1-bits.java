class Solution {
    public int[] sortByBits(int[] arr) {
        Integer[] ans = Arrays.stream(arr).boxed().toArray(Integer[]::new);
        Arrays.sort(ans, (n1, n2) -> {
                Integer n1Ones = 0, num = n1;
                while(num > 0){
                    num &= (num - 1);
                    n1Ones++;
                }
               
                Integer n2Ones = 0;
                num = n2;
                while(num > 0){
                    num &= (num - 1);
                    n2Ones++;
                }
               
               if(n1Ones == n2Ones)
                   return n1 - n2;
               else
                   return n1Ones - n2Ones;
        });
        return Arrays.stream(ans).mapToInt(Integer::intValue).toArray();
        
    }
}