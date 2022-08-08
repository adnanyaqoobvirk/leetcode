class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        if n == 1:
            return True
        
        for f in [2, 3, 5]:
            nn, r = divmod(n, f)
            if r == 0 and self.isUgly(nn):
                return True
        return False