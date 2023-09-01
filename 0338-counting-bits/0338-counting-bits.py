class Solution:
    def countBits(self, n: int) -> List[int]:
        res, p = [0], 0
        for num in range(1, n + 1):
            if 2 ** p == num:
                res.append(1)
                p += 1
            else:
                lp = 2 ** (p - 1)
                res.append(res[lp] + res[num - lp])
        return res