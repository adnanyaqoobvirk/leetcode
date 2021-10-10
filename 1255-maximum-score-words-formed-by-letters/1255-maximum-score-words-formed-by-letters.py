class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        counts = Counter(letters)
        n = len(words)
        maxScore = 0
        for num in range(1 << (n + 1)):
            currCounts = counts.copy()
            currScore = 0
            for i in range(n):
                if num & (1 << i):
                    tmpScore = 0
                    for j in range(len(words[i])):
                        c = words[i][j]
                        tmpScore += score[ord(c) - ord('a')]
                        if not currCounts[c]:
                            break
                        currCounts[c] -= 1
                    else:
                        currScore += tmpScore
                        continue
                    
                    for k in range(j):
                        currCounts[words[i][k]] += 1
            maxScore = max(maxScore, currScore)
        return maxScore
                