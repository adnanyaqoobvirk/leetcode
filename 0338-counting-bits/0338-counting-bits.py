class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for num in range(1, n + 1):
            res.append(res[num & (num - 1)] + 1)
        return res