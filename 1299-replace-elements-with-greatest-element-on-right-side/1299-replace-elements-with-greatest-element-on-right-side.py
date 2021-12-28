class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1
        for i in reversed(range(len(arr))):
            arr[i], greatest = greatest, max(arr[i], greatest)
        return arr