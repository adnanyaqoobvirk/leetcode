class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        smaller = [n] * n
        stack = []
        for i in reversed(range(n)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            if stack:
                smaller[i] = stack[-1]
            
            stack.append(i)
        
        ans = 0
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            
            ans = max(
                ans, 
                heights[i] * (smaller[i] if not stack else smaller[i] - stack[-1] - 1)
            )
            stack.append(i)
        
        return ans