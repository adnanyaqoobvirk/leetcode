class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        diff = min(arr[1] - arr[0], arr[2] - arr[1])
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return arr[i + 1] - arr[i] - diff + arr[i]
        return arr[0]