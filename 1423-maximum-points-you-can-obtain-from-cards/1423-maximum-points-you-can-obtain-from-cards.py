class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        
        if k == n:
            return total
        
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])
        
        nk = n - k
        max_score = curr_total = 0
        for i in range(n):
            if i < nk:
                curr_total += cardPoints[i]
            else:
                max_score = max(max_score, total - curr_total)
                curr_total += cardPoints[i]
                curr_total -= cardPoints[i - nk]
        return max(max_score, total - curr_total)