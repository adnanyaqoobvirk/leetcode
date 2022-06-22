class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        scounts = Counter(s)
        for ch, count in Counter(t).items():
            if scounts[ch] != count:
                return ch