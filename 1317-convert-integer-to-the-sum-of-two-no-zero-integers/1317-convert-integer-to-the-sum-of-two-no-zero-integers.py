class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        if n <= 9:
            return [n - 1, 1]

        x = n
        y = 0
        p = 1
        c = 0
        while x > 9:
            x, r = divmod(x, 10)
            if r - c <= 1:
                y += 2 * p
                c = 1
            else:
                y += p
                c = 0
            p *= 10

        return [n - y, y]