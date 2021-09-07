class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr[-1], mx = -1, arr[-1]
        for i in range(len(arr) - 2, -1, -1):
            arr[i], mx = mx, max(mx, arr[i])
        return arr