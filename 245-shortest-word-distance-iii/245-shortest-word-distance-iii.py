class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1hash, w2hash = hash(word1), hash(word2)
        p = phash = None
        distance = float('inf')
        for i, whash in enumerate(map(hash, wordsDict)):
            if whash == w1hash or whash == w2hash:
                if p is not None and (w1hash == w2hash or whash != phash):
                    distance = min(abs(i - p), distance)
                p, phash = i, whash
        return distance