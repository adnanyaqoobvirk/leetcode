class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:    
        MOD = 10**9 + 7
        prev, curr = [0] * (target + 1), [0] * (target + 1)
        prev[0] = 1
        for dice in reversed(range(n)):
            for remaining in range(1, target + 1):
                for face in range(1, min(remaining + 1, k + 1)):
                    curr[remaining] += prev[remaining - face]
                curr[remaining] %= MOD
            prev, curr = curr, [0] * (target + 1)
        return prev[target]