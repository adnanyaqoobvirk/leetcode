class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freqs = Counter(words)
        swords = [(-freq, word) for word, freq in freqs.items()]
        swords.sort()
        return [swords[i][1] for i in range(k)]