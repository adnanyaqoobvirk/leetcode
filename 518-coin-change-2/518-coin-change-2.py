class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev, curr = [0] * (amount + 1), [0] * (amount + 1)
        prev[0] = curr[0] = 1
        for pos in reversed(range(len(coins))):
            for remaining in range(1, amount + 1):
                curr[remaining] = (
                    ((curr[remaining - coins[pos]]) if remaining >= coins[pos] else 0)
                    + prev[remaining]
                )
            prev, curr = curr, [0] * (amount + 1)
            curr[0] = 1
        return prev[amount]