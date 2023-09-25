class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scounts = Counter(s)
        tcounts = Counter(t)
        
        for c, count in tcounts.items():
            if scounts[c] != count:
                return c