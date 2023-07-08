class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        pairs = sorted(weights[i] + weights[i + 1] for i in range(n - 1))
        return sum(pairs[n - k:]) - sum(pairs[0:k - 1])
        