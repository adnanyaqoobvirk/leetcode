class Solution:
    def minimumSum(self, num: int) -> int:
        digits = []
        for i in range(4):
            num, d = divmod(num, 10)
            digits.append(d)
        digits.sort()
        
        num1 = num2 = 0
        for i in range(4):
            if i & 1:
                num1 = num1 * 10 + digits[i]
            else:
                num2 = num2 * 10 + digits[i]
        return num1 + num2