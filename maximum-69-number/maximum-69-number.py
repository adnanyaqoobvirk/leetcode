class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        msb = None
        i = 0
        while n > 0:
            n, d = divmod(n, 10)
            if d == 6:
                msb = i
            i += 1
        return num if msb is None else num + ((10 ** msb) * 3)