class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] > arr[1]:
            return False
        
        prev = arr[0]
        for i in range(1, len(arr)):
            if arr[i] <= prev:
                break
            prev = arr[i]
        else:
            return False
        
        for i in range(i, len(arr)):
            if arr[i] >= prev:
                return False
            prev = arr[i]
        return True