class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        total = 0
        for i in range(n):
            idx_arr_cnt = (n - i) * (i + 1)
            idx_odd_arr_cnt = (idx_arr_cnt + 1) // 2
            total += idx_odd_arr_cnt * arr[i]
        return total