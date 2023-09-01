class Solution:
    def countBits(self, n: int) -> List[int]:
        res, p1, p2 = [0], 1, 0
        for num in range(1, n + 1):
            if p1 == num:
                res.append(1)
                p2, p1 = p1, p1 * 2
            else:
                res.append(res[p2] + res[num - p2])
        return res