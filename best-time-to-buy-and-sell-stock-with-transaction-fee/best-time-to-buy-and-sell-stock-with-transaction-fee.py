class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        prev, curr = [0, 0], [0, 0]
        for pos in reversed(range(n)):
            for bought in range(2):
                do_nothing = prev[bought]

                if bought:
                    do_something = prices[pos] + prev[0]
                else:
                    do_something = prev[1] - prices[pos] - fee

                curr[bought] = max(
                    do_nothing,
                    do_something
                )
            prev, curr = curr, prev
        return prev[0]