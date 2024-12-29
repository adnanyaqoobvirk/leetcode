class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        @cache
        def dp(i: int, j: int) -> int:
            if j == n:
                return 1
            if i == m:
                return 0
            return freq[i][target[j]] * dp(i + 1, j + 1) % MOD + dp(i + 1, j) % MOD

        m, n = len(words[0]), len(target)
        MOD = 10**9 + 7
        freq = [defaultdict(int) for _ in range(m)]
        for word in words:
            for i, c in enumerate(word):
                freq[i][c] += 1
        return dp(0, 0)