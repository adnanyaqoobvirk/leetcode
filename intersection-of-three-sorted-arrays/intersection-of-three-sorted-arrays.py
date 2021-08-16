class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        int_count = {num: 1 for num in arr1}
        
        for num in arr2:
            int_count[num] = int_count.get(num, 0) + 1
        
        return [num for num in arr3 if int_count.get(num, 0) == 2]