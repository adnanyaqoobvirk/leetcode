class Solution:
    def confusingNumber(self, n: int) -> bool:
        invalids = {2, 3, 4, 5, 7}
        valids = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
        new = 0
        i = n
        while i > 0:
            i, d = divmod(i, 10)
            if d in invalids:
                return False
            new = new * 10 + valids[d]
        return new != n
        