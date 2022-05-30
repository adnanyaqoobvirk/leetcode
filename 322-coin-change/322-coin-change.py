class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(pos: int, remaining: int) -> int:
            if remaining == 0:
                return 0
            
            if pos >= n or remaining < 0:
                return float('inf')
        
            coin_count = float('inf')
            for i in range(pos, n):
                coin_count = min(
                    coin_count,
                    helper(i, remaining - coins[i]) + 1
                )
            return coin_count
        
        n = len(coins)
        ans = helper(0, amount)
        return -1 if ans == float('inf') else ans