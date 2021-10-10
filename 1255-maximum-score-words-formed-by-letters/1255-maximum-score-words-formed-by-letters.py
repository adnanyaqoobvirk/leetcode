class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def possible(word: str) -> bool:
            for c, v in Counter(word).items():
                if counts[c] < v:
                    return False
            return True
        
        def backtrack(pos: int, maxScore: int) -> int:
            currMaxScore = maxScore
            for i in range(pos, n):
                if possible(words[i]):
                    currScore = 0
                    for c in words[i]:
                        currScore += score[ord(c) - ord('a')]
                        counts[c] -= 1
                    
                    currMaxScore = max(currMaxScore, backtrack(i + 1, maxScore + currScore))
                    
                    for c in words[i]:
                        counts[c] += 1
            return currMaxScore                    
            
        n = len(words)
        counts = Counter(letters)
        return backtrack(0, 0)