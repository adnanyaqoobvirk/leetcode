class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        ans = []
        for price in reversed(prices):
            while stack and stack[-1] > price:
                stack.pop()
                
            ans.append(price if not stack else price - stack[-1])
            
            stack.append(price)
        return reversed(ans)