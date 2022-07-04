class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def helper(remaining: int) -> int:
            if remaining < 0:
                return inf
            
            if remaining == 0:
                return 0
            
            ans = inf
            for coin in coins:
                ans = min(
                    ans, helper(remaining - coin)
                )
            return ans + 1
        
        n = len(coins)
        ans = helper(amount)
        return ans if ans != inf else -1