class Solution:
    def findNthDigit(self, n: int) -> int:
        max_num = 0
        dcount = 0
        tdigits = 0
        while tdigits + (9 * 10**dcount * (dcount + 1)) < n:
            tdigits += 9 * (10**dcount) * (dcount + 1)
            dcount += 1
            max_num = max_num * 10 + 9
        d, r = divmod(n - tdigits, dcount + 1)
        if r == 0:
            return (max_num + d) % 10
        else:
            num = max_num + d + 1
            for _ in range(dcount - r + 1):
                num //= 10
            return num % 10
        
        