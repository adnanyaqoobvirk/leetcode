class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        aba = abc = 6
        for _ in range(n - 1):
            abc, aba = (2 * abc + 2 * aba) % MOD, (2 * abc + 3 * aba) % MOD
        return (aba + abc) % MOD