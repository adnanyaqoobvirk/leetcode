class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr = set(arr)
        miss_count = 0
        for num in range(1, max(arr) + k + 1):
            if num not in arr:
                miss_count += 1
                if miss_count == k:
                    return num