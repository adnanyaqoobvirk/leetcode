class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         @cache
#         def helper(pos: int, bought: int) -> int:
#             if pos == n:
#                 return -inf
            
#             if bought:
#                 return max(
#                     prices[pos],
#                     helper(pos + 1, True)
#                 )
#             else:
#                 return max(
#                     helper(pos + 1, False),
#                     -prices[pos] + helper(pos + 1, True)
#                 )
        
#         n = len(prices)
#         ans = helper(0, 0)
#         return 0 if ans < 0 else ans
    
        n = len(prices)
        curr_bought = curr_not_bought = -inf
        for pos in reversed(range(n)):
            curr_bought, curr_not_bought = max(
                prices[pos],
                curr_bought
            ), max(
                curr_not_bought,
                -prices[pos] + curr_bought
            )
        return 0 if curr_not_bought < 0 else curr_not_bought