class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = Counter(s)
        for c in t:
            counts[c] -= 1
        return sum(abs(v) for v in counts.values()) == 0
            
            