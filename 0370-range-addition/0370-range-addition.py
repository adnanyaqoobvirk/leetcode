class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        diff_array = [0] * length
        for start, end, inc in updates:
            diff_array[start] += inc
            if end < length - 1:
                diff_array[end + 1] -= inc
        for i in range(1, length):
            diff_array[i] += diff_array[i - 1]
        return diff_array
