# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        c = set(range(n))
        while len(c) > 1:
            a, b = c.pop(), c.pop()
            if knows(a, b):
                c.add(b)
            else:
                c.add(a)
        a = c.pop()
        for b in range(n):
            if a != b:
                if not knows(b, a):
                    return -1
                if knows(a, b):
                    return -1
        return a