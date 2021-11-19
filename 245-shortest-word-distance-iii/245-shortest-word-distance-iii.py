class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        w1hash, w2hash = hash(word1), hash(word2)
        w1loc = []
        w2loc = []
        for i, whash in enumerate(map(hash, wordsDict)):
            if whash == w1hash:
                w1loc.append(i)
            elif whash == w2hash:
                w2loc.append(i)
        
        p0 = p1 = 0
        distance = float('inf')
        
        if w1hash == w2hash:
            w2loc = w1loc
            p1 = 1
        
        ll0, ll1 = len(w1loc), len(w2loc)
        while p0 < ll0 and p1 < ll1:
            distance = min(abs(w1loc[p0] - w2loc[p1]), distance)
            
            if w1hash != w2hash:
                if w1loc[p0] < w2loc[p1]:
                    p0 += 1
                else:
                    p1 += 1
            else:
                p0, p1 = p1, p1 + 1
        return distance