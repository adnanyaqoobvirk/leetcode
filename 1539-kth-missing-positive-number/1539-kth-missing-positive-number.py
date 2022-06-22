class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = len(arr) - 1
        
        miss_count = pos = 0
        for num in range(1, max(arr) + k + 1):
            if num != arr[pos]:
                miss_count += 1
                if miss_count == k:
                    return num
            elif pos < n:
                pos += 1