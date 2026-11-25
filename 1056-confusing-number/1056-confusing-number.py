class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalids = set([2, 3, 4, 5, 7])
        m = n
        rn = 0
        while m > 0:
            m, d = divmod(m, 10)

            if d in invalids:
                return False
            elif d == 6:
                d = 9
                print(d)
            elif d == 9:
                d = 6
                
            rn = rn * 10 + d
        return rn != n
