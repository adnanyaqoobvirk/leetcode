class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        words = {}
        for i, word in enumerate(wordsDict):
            words.setdefault(word, []).append(i)
        
        distance = float('inf')
        for d1 in words[word1]:
            for d2 in words[word2]:
                distance = min(abs(d1 - d2), distance)
        return distance