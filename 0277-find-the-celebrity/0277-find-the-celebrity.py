# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        x = 0
        for y in range(1, n):
            if knows(x, y):
                x = y
        
        count = 0
        for y in range(n):
            if not knows(x, y) and knows(y, x):
                count += 1
        
        return -1 if count != n - 1 else x