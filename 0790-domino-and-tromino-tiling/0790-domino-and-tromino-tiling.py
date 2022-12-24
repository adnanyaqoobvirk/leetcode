class Solution:
    def numTilings(self, n: int) -> int:
        if n <= 2:
            return n
    
        MOD = 10**9 + 7
        pprev, prev, curr = [1, 1], [2, 2], [0, 0]
        for pos in range(n - 2):
            curr[0] = (
                prev[0] +
                prev[1]
            ) % MOD 
            curr[1] = (
                prev[1] + 
                pprev[1] + 
                2 * pprev[0]
            ) % MOD
            pprev, prev, curr = prev, curr, [0, 0]
        return prev[1]