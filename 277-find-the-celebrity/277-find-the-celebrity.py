# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        @cache
        def helper(a: int, b: int) -> bool:
            return knows(a, b)
        
        celebrity = 0
        for p in range(1, n):
            if helper(celebrity, p):
                celebrity = p
                
        for p in range(n):
            if p != celebrity and (helper(celebrity, p) or not helper(p, celebrity)):
                return -1
        return celebrity