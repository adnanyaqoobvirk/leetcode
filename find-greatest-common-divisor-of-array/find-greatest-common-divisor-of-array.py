class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a: int, b: int) -> int:
            if b == 0:
                return a
            else:
                return gcd(b, a % b)
            
        min_num = None
        max_num = None
        for num in nums:
            if min_num is None or num < min_num:
                min_num = num
            
            if max_num is None or num > max_num:
                max_num = num
                
        return gcd(min_num, max_num)