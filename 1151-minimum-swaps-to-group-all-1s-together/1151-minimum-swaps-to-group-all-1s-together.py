class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n, counts = len(data), Counter(data)
        
        min_zero_count = 0
        for i in range(counts[1]):
            if data[i] == 0:
                min_zero_count += 1
        
        zero_count, one_count = min_zero_count, counts[1]
        for i in range(counts[1], n):
            if data[i] == 0:
                zero_count += 1
            if data[i - one_count] == 0:
                zero_count -= 1
            min_zero_count = min(min_zero_count, zero_count)
        return min_zero_count