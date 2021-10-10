class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def backtrack(pos: int, maxScore: int) -> int:
            currMaxScore = maxScore
            for i in range(pos, n):
                currScore = 0
                for j in range(len(words[i])):
                    c = words[i][j]
                    currScore += score[ord(c) - ord('a')]
                    if not counts[c]:
                        break
                    counts[c] -= 1
                else:
                    currMaxScore = max(currMaxScore, backtrack(i + 1, maxScore + currScore))
                    j += 1
                    
                for j in range(j):
                    counts[words[i][j]] += 1
            return currMaxScore                    
            
        n = len(words)
        counts = Counter(letters)
        return backtrack(0, 0)
                