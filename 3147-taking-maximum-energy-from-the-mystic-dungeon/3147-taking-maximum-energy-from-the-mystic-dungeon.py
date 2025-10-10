class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = len(energy)
        dp = [0] * m
        max_energy = -inf
        for i in reversed(range(m)):
            dp[i] = energy[i] if i + k >= m else energy[i] + dp[i + k]
            max_energy = max(max_energy, dp[i])
        return max_energy