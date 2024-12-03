# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        a = 0
        for b in range(1, n):
            if knows(a, b):
                a = b
        for b in range(n):
            if a != b:
                if not knows(b, a):
                    return -1
                if knows(a, b):
                    return -1
        return a