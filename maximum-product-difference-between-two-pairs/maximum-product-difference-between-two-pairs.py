class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        first_min = second_min = first_max = second_max = None
        for num in nums:
            if first_min is None:
                first_min = num
            elif num < first_min:
                first_min, second_min = num, first_min
            elif second_min is None or num < second_min:
                second_min = num
            
            if first_max is None:
                first_max = num
            elif num > first_max:
                first_max, second_max = num, first_max
            elif second_max is None or num > second_max:
                second_max = num
        return first_max * second_max - first_min * second_min
            
            
        
        