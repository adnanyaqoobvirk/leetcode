class Solution:
    def countBits(self, n: int) -> List[int]:
        res, p, lp1, lp2 = [0], 0, 1, 0
        for num in range(1, n + 1):
            if lp1 == num:
                res.append(1)
                p += 1
                lp1, lp2 = 2 ** p, 2 ** (p - 1)
            else:
                res.append(res[lp2] + res[num - lp2])
        return res