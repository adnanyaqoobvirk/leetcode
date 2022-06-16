class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lo, hi = 1, len(arr) - 2
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid - 1] > arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo if arr[lo - 1] < arr[lo] > arr[lo + 1] else lo - 1