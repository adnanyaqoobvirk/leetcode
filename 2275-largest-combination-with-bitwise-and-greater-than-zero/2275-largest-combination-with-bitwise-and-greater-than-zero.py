class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counts = [0] * 32
        for c in candidates:
            for i in range(32):
                if c == 0:
                    break
                if c & 1:
                    counts[i] += 1
                c >>= 1
        return max(counts)
            