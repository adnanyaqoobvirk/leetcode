class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a = (ax2 - ax1) * (ay2 - ay1)
        b = (bx2 - bx1) * (by2 - by1)
        
        xo = min(bx2, ax2) - max(bx1, ax1)
        yo = min(by2, ay2) - max(by1, ay1)
        
        if xo > 0 and yo > 0:
            return a + b - (xo * yo)
        else:
            return a + b