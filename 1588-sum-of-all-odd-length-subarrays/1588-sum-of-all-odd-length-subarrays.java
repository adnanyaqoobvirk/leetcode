class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int ans = 0;
        for(int i = 0; i < arr.length; i++){
            int total = 0;
            for(int j = i; j < arr.length; j++){
                total += arr[j];
                if((i - j) % 2 == 0)
                    ans += total;
            }
        }
        return ans;
    }
}