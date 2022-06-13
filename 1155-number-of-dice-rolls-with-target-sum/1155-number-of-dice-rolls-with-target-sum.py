class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(dice: int, remaining: int) -> int:
            if dice == n:
                return remaining == 0
            
            ways = 0
            for face in range(1, k + 1):
                ways += helper(dice + 1, remaining - face)
            return ways % MOD
        MOD = 10**9 + 7
        return helper(0, target)
        