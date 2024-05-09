class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        
        ans = 0
        for i in range(k):
            ans += max(0, happiness[-(i + 1)] - i)
        return ans