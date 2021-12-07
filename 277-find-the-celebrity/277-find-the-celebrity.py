# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        @cache
        def helper(a: int, b: int) -> bool:
            return knows(a, b)
        
        p1, p2 = 0, 1
        while p1 < n and p2 < n:
            if helper(p1, p2):
                p1 = max(p1, p2) + 1
            else:
                p2 = max(p1, p2) + 1
                
        p = min(p1, p2)
        for i in range(n):
            if i != p and (helper(p, i) or not helper(i, p)):
                return -1
        return p