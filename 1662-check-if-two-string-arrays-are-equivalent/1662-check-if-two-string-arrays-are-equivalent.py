class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        n = len(word2)
        
        i = j = 0
        for w in word1:
            for c in w:
                if j == len(word2[i]):
                    i += 1
                    j = 0
                
                if i == n:
                    return False
                
                if word2[i][j] != c:
                    return False
                
                j += 1
        return i == len(word2) - 1 and j == len(word2[-1])
                