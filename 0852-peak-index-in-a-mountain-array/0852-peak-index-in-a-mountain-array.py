class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            i = l + r >> 1
            if arr[i - 1] < arr[i] > arr[i + 1]:
                return i
            elif arr[i] < arr[i + 1]:
                l = i
            else:
                r = i
        return -1