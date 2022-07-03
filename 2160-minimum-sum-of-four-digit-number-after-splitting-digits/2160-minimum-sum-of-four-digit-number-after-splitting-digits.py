class Solution:
    def minimumSum(self, num: int) -> int:
        num1 = num2 = 0
        for i, d in enumerate(sorted(str(num))):
            if i & 1:
                num1 = num1 * 10 + int(d)
            else:
                num2 = num2 * 10 + int(d)
        return num1 + num2