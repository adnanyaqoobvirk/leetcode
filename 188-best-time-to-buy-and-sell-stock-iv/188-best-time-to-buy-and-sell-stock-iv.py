class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        prev, curr = [[0] * (k + 1) for _ in range(2)], [[0] * (k + 1) for _ in range(2)]
        for pos in reversed(range(n)):
            for bought in reversed(range(2)):
                for t in range(1, k + 1):
                    buy_stock = 0
                    if not bought:
                        buy_stock = -prices[pos] + prev[1][t]

                    skip = prev[bought][t]

                    sell_stock = 0
                    if bought:
                        sell_stock = prices[pos] + prev[0][t - 1]

                    curr[bought][t] = max(
                        buy_stock,
                        skip,
                        sell_stock
                    )
            prev, curr = curr, prev
        return prev[0][k]