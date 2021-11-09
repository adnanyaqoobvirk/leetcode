class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        dist = float('inf')
        w1 = w2 = None
        for i, word in enumerate(wordsDict):
            if word == word1:
                w1 = i
            elif word == word2:
                w2 = i
            
            if w1 is not None and w2 is not None:
                dist = min(abs(w1 - w2), dist)
        return dist