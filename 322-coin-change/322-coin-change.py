class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(pos: int, total: int) -> int:
            if pos >= n or total > amount:
                return float('inf')
            
            if total == amount:
                return 0
            
            return min(
                helper(pos, coins[pos] + total) + 1,
                helper(pos + 1, coins[pos] + total) + 1,
                helper(pos + 1, total)
            )
        n = len(coins)
        ans = helper(0, 0)
        return -1 if ans == float('inf') else ans