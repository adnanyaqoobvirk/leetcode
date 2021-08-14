class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        total = 0
        for i in range(len(arr)):
            current_sum = 0
            for j in range(i, len(arr)):
                current_sum += arr[j]
                if (j - i) % 2 == 0:
                    total += current_sum
        return total