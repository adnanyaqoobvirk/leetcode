class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(m: int) -> float:
            if m == 0:
                return 1

            if m & 1:
                return x * helper(m - 1)
            else:
                ans = helper(m // 2)
                return ans * ans
        return 1 / helper(abs(n)) if n < 0 else helper(abs(n))