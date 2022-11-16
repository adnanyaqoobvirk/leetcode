# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 0, n
        while lo + 1 < hi:
            guess = lo + (hi - lo) // 2
            if isBadVersion(guess):
                hi = guess
            else:
                lo = guess
        return hi