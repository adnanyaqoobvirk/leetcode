class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = None
        max_num = None
        for num in nums:
            if min_num is None or num < min_num:
                min_num = num
            
            if max_num is None or num > max_num:
                max_num = num
                
        while max_num > 0:
            min_num, max_num = max_num, min_num % max_num
        return min_num