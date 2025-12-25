class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        max_sum = 0
        for i in range(k):
            max_sum += happiness[i] - i
        return max_sum