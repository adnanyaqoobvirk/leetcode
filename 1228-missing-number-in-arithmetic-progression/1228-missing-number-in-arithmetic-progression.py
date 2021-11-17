class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = (arr[-1] - arr[0]) // len(arr)
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if arr[mid] == arr[0] + diff * mid:
                left = mid + 1
            else:
                right = mid
        return arr[0] + left * diff