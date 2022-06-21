class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0
        for i in range(n):
            curr_total = 0
            for j in range(i, n):
                curr_total += arr[j]
                if (j - i + 1) & 1:
                    ans += curr_total
        return ans