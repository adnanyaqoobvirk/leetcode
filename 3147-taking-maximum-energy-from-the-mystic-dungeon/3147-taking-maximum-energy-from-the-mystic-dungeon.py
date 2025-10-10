class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        m = len(energy)
        max_energy = -inf
        for i in range(m - k, m):
            total = 0
            for j in range(i, -1, -k):
                total += energy[j]
                max_energy = max(max_energy, total)
        return max_energy