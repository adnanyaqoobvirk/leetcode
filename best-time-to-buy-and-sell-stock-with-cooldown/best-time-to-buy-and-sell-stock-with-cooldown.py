class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pprev, prev, curr = [0] * 2, [0] * 2, [0] * 2
        for pos in reversed(range(n)):
            for bought in reversed(range(2)):
                curr[bought] = max(
                    -prices[pos] + prev[1],
                    prev[bought],
                    (prices[pos] + pprev[0]) if bought else 0
                )
            pprev, prev, curr = prev, curr, pprev
        return prev[0]