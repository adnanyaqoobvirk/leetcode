class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        ans, product = 1, x
        while n > 0:
            if n & 1:
                ans *= product
            product *= product
            n //= 2
            
        return ans
        
        
        