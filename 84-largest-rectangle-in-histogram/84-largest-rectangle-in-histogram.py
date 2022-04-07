class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack, largest = [], 0
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                start, height = stack.pop()
                largest = max(largest, (i - start) * height)
            stack.append((start, h))
        return largest