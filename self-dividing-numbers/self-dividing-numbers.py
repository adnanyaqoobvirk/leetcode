class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            n = num
            while n > 1:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    break
                n = n // 10
            if n <= 1:
                res.append(num)
        return res