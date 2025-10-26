class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        d, r = divmod(sum, 9)
        if r == 0 and d > num:
            return ""
        elif r > 0 and d >= num:
            return ""
            
        res = ["9"] * d
        if r > 0:
            res.append(str(r))
        for _ in range(d + 1, num):
            res.append("0")
        return "".join(res)