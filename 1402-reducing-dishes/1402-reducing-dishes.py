class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        maxltc = 0
        for i in range(len(satisfaction)):
            ltc = 0
            for idx, j in enumerate(range(i, len(satisfaction)), 1):
                ltc += satisfaction[j] * idx
            maxltc = max(maxltc, ltc)
        return maxltc