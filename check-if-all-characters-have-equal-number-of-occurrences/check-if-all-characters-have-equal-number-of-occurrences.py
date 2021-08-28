class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
            
        count = counts[c]
        for v in counts.values():
            if v != count:
                return False
        
        return True