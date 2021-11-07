class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        res = [0] * 400
        for i1, d1 in enumerate(map(int, reversed(num1))):
            carry = 0
            for i2, d2 in enumerate(map(int, reversed(num2))):
                carry, d = divmod(d1 * d2 + carry, 10)
                c, res[i1 + i2] = divmod(res[i1 + i2] + d, 10) 
                carry += c
            if carry:
                res[i1 + i2 + 1] = carry
        
        leading_zeros = True
        ans = ""
        for d in reversed(res):
            if leading_zeros and d:
                leading_zeros = False
            if not leading_zeros:
                ans += str(d)
        return ans