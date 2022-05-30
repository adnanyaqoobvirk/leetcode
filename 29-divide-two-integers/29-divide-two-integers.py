class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT, MIN_INT = 2**31 - 1, -(2**31)
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        negative = False
        if dividend < 0 and divisor < 0:
            dividend = -dividend
            divisor = -divisor
        elif dividend < 0:
            negative = True
            dividend = -dividend
        elif divisor < 0:
            negative = True
            divisor = -divisor
        
        q = 0
        while dividend >= divisor:
            iq = 1
            divd, divs = dividend, divisor
            while divd >= divs:
                divd -= divs
                iq <<= 1
                divs <<= 1
            q += iq >> 1
            dividend -= divs >> 1
            
        return -q if negative else q