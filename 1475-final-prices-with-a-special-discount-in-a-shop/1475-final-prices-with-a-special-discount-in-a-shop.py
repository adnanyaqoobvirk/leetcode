class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        for i in reversed(range(len(prices))):
            price = prices[i]
            
            while stack and stack[-1] > price:
                stack.pop()
                
            prices[i] = price if not stack else price - stack[-1]
            
            stack.append(price)
        return prices