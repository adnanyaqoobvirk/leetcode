class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        while n > 1:
            d, r = divmod(n, 2)
            matches += d
            n = d + r
        return matches
        