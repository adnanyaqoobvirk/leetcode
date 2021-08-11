class Solution:
    def longestCommomSubsequence(self, arrays: List[List[int]]) -> List[int]:
        def search(array: List[int], num: int) -> bool:
            left, right = 0, len(array)
            while left < right:
                mid = left + (right - left) // 2
                if array[mid] == num:
                    return True
                elif array[mid] > num:
                    right = mid
                else:
                    left = mid + 1
            return False
        
        smallest_array = None
        for array in arrays:
            if smallest_array is None or len(smallest_array) > len(array):
                smallest_array = array
        
        result = []
        for num in smallest_array:
            for array in arrays:
                if array == smallest_array:
                    continue
                if not search(array, num):
                    break
            else:
                result.append(num)
        return result