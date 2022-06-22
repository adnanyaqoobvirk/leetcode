class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid = lo + (hi - lo) // 2
            miss_count = arr[mid] - mid - 1
            if miss_count >= k:
                hi = mid
            else:
                lo = mid + 1
        return arr[lo - 1] + (k - arr[lo - 1] + lo)