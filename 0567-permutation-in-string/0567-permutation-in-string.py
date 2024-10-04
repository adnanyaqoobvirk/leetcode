class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        
        counts1 = [0] * 26
        counts2 = [0] * 26

        for i in range(n1):
            counts1[ord(s1[i]) - ord('a')] += 1
            counts2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if counts1[i] == counts2[i]:
                matches += 1
        
        for i in range(n1, n2):
            if matches == 26:
                return True
            
            counts2[ord(s2[i]) - ord('a')] += 1
            if counts2[ord(s2[i]) - ord('a')] == counts1[ord(s2[i]) - ord('a')]:
                matches += 1
            elif counts2[ord(s2[i]) - ord('a')] - 1 == counts1[ord(s2[i]) - ord('a')]:
                matches -= 1
            
            counts2[ord(s2[i - n1]) - ord('a')] -= 1
            if counts2[ord(s2[i - n1]) - ord('a')] == counts1[ord(s2[i - n1]) - ord('a')]:
                matches += 1
            elif counts2[ord(s2[i]) - ord('a')] + 1 == counts1[ord(s2[i]) - ord('a')]:
                matches -= 1
        return False