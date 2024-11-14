class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(-inf)
        stack = []
        ans = 0
        for i in range(len(heights)):
            j = i
            while stack and stack[-1][1] > heights[i]:
                j, v = stack.pop()
                ans = max(ans, v * (i - j))
            stack.append((j, heights[i]))
        return ans