class Solution:
    def getSum(self, a: int, b: int) -> int:
        def sum(x: int, y: int) -> int:
            if y == 0:
                return x
            
            return sum(x ^ y, (x & y) << 1)

        def subtract(x: int, y: int) -> int:
            if y == 0:
                return x
            
            return subtract(x ^ y, (~x & y) << 1)

        if a < 0 and b < 0:
            return -sum(-a, -b)
        
        if abs(a) < abs(b):
            a, b = b, a
        
        if a < 0:
            return -subtract(-a, b)
        
        if b < 0:
            return subtract(a, -b)
        
        return sum(a, b)