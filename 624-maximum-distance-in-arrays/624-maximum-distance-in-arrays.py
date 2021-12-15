class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_val, max_val, max_d = arrays[0][0], arrays[0][-1], 0
        for i in range(1, len(arrays)):
            arr = arrays[i]
            max_d = max(max_d, abs(arr[-1] - min_val), abs(arr[0] - max_val))
            min_val, max_val = min(min_val, arr[0]), max(max_val, arr[-1])
        return max_d