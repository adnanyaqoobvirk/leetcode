class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, num in enumerate(arr):
            if num == i:
                return i
        return -1