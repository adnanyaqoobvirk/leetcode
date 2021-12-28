class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 or arr[0] >= arr[1]:
            return False
        
        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                break
            
        for j in range(i, len(arr)):
            if arr[j] >= arr[j - 1]:
                return False
        
        return True