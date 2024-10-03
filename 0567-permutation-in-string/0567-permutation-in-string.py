class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        
        counts1 = Counter(s1)
        counts2 = Counter(s2[:n1])

        if counts1 == counts2:
            return True
        
        for i in range(n1, n2):
            counts2[s2[i]] += 1
            counts2[s2[i - n1]] -= 1
        
            if counts1 == counts2:
                return True
        return False