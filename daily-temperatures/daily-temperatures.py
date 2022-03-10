class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans, stack = [0] * len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans