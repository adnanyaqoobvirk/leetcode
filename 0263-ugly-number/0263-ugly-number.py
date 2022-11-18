class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while True:
                d, r = divmod(n, p)
                if r != 0:
                    break
                n = d
        return n == 1