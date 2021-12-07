# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        celebrity = 0
        for p in range(1, n):
            if knows(celebrity, p):
                celebrity = p
                
        for p in range(n):
            if p != celebrity and (knows(celebrity, p) or not knows(p, celebrity)):
                return -1
        return celebrity