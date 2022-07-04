class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        
        prev, curr = [0] * (amount + 1), [0] * (amount + 1)
        prev[0] = curr[0] = 1
        for pos in reversed(range(n)):
            for remaining in range(amount + 1):
                if remaining - coins[pos] < 0:
                    curr[remaining] = prev[remaining]
                else:
                    curr[remaining] = curr[remaining - coins[pos]] + prev[remaining]
            prev, curr = curr, prev
        return prev[amount]
                