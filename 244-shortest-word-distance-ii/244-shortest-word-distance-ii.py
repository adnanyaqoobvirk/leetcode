class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.words = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.words[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        distance = float('inf')
        l0, l1 = self.words[word1], self.words[word2]
        ll0, ll1 = len(l0), len(l1)
        p0 = p1 = 0
        while p0 < ll0 and p1 < ll1:
            distance = min(abs(l0[p0] - l1[p1]), distance)
            if l0[p0] < l1[p1]:
                p0 += 1
            else:
                p1 += 1
        return distance
    
# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)