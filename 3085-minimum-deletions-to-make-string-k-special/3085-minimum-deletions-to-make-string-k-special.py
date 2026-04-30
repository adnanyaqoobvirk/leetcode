class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = sorted(Counter(word).items(), key=lambda x: x[1])
        min_dels = len(word)
        n = len(freq)
        left_dels = 0
        for i in range(n):
            right_dels = 0
            for j in range(i + 1, n):
                if freq[j][1] - freq[i][1] > k:
                    right_dels += freq[j][1] - freq[i][1] - k
            min_dels = min(min_dels, left_dels + right_dels)
            left_dels += freq[i][1]
        return min_dels