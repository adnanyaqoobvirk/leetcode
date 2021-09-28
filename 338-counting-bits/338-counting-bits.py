class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            idx, r = divmod(i, 2)
            ans[i] = ans[idx] + r
        return ans
            