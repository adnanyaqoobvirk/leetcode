class Solution:
    def myAtoi(self, s: str) -> int:
        MIN_ALLOWED = -2**31
        MAX_ALLOWED = 2**31 - 1
        DIGITS = set("0123456789")

        n = len(s)
        i = 0

        # skip white spaces
        while i < n and s[i] == " ":
            i += 1
        
        # check for sign
        sign = 1
        if i < n and (s[i] == "-" or s[i] == "+"):
            if s[i] == "-":
                sign = -1
            i += 1
        
        # skip leading zeros
        while i < n and s[i] == "0":
            i += 1
        
        # read the number
        num = 0
        while i < n and s[i] in DIGITS:
            num = num * 10 + int(s[i])
            
            if sign * num <= MIN_ALLOWED:
                return MIN_ALLOWED
            elif sign * num >= MAX_ALLOWED:
                return MAX_ALLOWED

            i += 1
        
        return sign * num