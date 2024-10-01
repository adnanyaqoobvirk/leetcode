class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_len = 0
        trues = 0
        falses = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                trues += 1
            else:
                falses += 1
            
            if min(trues, falses) > k:
                if answerKey[l] == 'T':
                    trues -= 1
                else:
                    falses -= 1
                l += 1
            
            max_len = max(max_len, r - l + 1)
        return max_len