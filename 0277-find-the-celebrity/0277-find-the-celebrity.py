# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        x, seen = 0, {}
        for y in range(1, n):
            seen[(x, y)] = knows(x, y)
            if seen[(x, y)]:
                x = y
        
        count = 0
        for y in range(n):
            xy = seen[(x, y)] if (x, y) in seen else knows(x, y)
            yx = seen[(y, x)] if (y, x) in seen else knows(y, x)
            if not xy and yx:
                count += 1
        
        return -1 if count != n - 1 else x