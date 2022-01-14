class Solution:
    def myAtoi(self, s: str) -> int:
        if not s: return 0
        
        neg = sign = False
        for i in range(len(s)):
            if s[i] == ' ':
                if sign: return 0
                continue
            elif s[i] == '+':
                if sign: return 0
                sign = True
            elif s[i] == '-':
                if sign: return 0
                sign = neg = True
            else: break
        
        digits, integer = {str(d):d for d in range(10)}, 0
        for j in range(i, len(s)):
            if s[j] in digits: integer = integer * 10 + digits[s[j]]
            else: break
                
        if integer > 0 and neg: integer *= -1
        
        if integer < -(2**31): return -(2**31)
        elif integer > (2**31 - 1): return (2**31 - 1)
        else: return integer