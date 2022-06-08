class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n, one_count = len(data), sum(data)
        
        min_zero_count = 0
        for i in range(one_count):
            if data[i] == 0:
                min_zero_count += 1
        
        zero_count, left = min_zero_count, 0
        for right in range(one_count, n):
            if data[right] == 0:
                zero_count += 1
            if data[left] == 0:
                zero_count -= 1
            min_zero_count = min(min_zero_count, zero_count)
            left += 1
        return min_zero_count