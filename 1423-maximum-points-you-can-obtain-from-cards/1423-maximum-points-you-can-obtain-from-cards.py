class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if k == len(cardPoints):
            return sum(cardPoints)
        
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        
        prefixes = [0]
        prefix = 0
        for points in cardPoints:
            prefix += points
            prefixes.append(prefix)
        
        suffixes = [0]
        suffix = 0
        for points in reversed(cardPoints):
            suffix += points
            suffixes.append(suffix)
        
        max_score = 0
        for i in reversed(range(k + 1)):
            max_score = max(max_score, prefixes[i] + suffixes[k - i])
        return max_score