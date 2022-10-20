class FWord:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        
    def __lt__(self, other):
        return self.freq < other.freq or (
            self.freq == other.freq and self.word > other.word
        )
    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        h = []
        for word, freq in Counter(words).items():
            fword = FWord(word, freq)
            heappush(h, fword)
            if len(h) > k:
                heappop(h)
        return [fword.word for fword in sorted(h, reverse = True)]