class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        w1_counts = sorted(Counter(word1).values())
        w2_counts = sorted(Counter(word2).values())
        
        if w1_counts != w2_counts:
            return False
        
        return set(word1) == set(word2)
        
        