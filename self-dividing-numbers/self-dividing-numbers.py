class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for num in range(left, right + 1):
            n = num
            sdn = True
            while sdn and n > 0:
                n, digit = divmod(n, 10)
                if digit == 0 or num % digit != 0:
                    sdn = False
            if sdn:
                res.append(num)
        return res