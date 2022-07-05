class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        for curr in range(len(height)):
            while stack and height[curr] > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                dist = curr - stack[-1] - 1
                bh = min(height[curr], height[stack[-1]]) - height[top]
                ans += dist * bh
            stack.append(curr)
        return ans