# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        nodes = {node for node in range(n)}
        for a in range(n):
            for b in range(a + 1, n):
                if knows(b, a):
                    nodes.discard(b)
                if knows(a, b):
                    nodes.discard(a)
        return next(iter(nodes)) if len(nodes) == 1 else -1