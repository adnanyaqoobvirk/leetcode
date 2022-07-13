class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int ans = 0;
        for(int i = 0; i < arr.length; i++){
            int subArrayCount = (arr.length - i) * (i + 1);
            int oddSubArrayCount = (subArrayCount + 1) / 2;
            ans += arr[i] * oddSubArrayCount;
        }
        return ans;
    }
}