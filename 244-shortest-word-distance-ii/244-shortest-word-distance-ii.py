class WordDistance:

    def __init__(self, wordsDict: List[str]):
        n = len(wordsDict)
        
        self.words = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.words[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        distance = float('inf')
        for i in self.words[word1]:
            for j in self.words[word2]:
                distance = min(abs(i - j), distance)
        return distance
    
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)