# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        for a in range(n):
            for b in range(n):
                if a != b:
                    if not knows(b, a) or knows(a, b):
                        break
            else:
                return a
        return -1