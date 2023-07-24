class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        ans, p = x, 1
        while p + p < n:
            ans *= ans
            p += p
        
        ans *= self.myPow(x, n - p)
        
        return ans