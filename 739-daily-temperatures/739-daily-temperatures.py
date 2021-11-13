class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        stack = []
        for temp in reversed(temperatures):
            diff = 1
            while stack and stack[-1][0] <= temp:
                diff += stack.pop()[1]
            
            if not stack:
                ans.append(0)
                stack.append((temp, 0))
            else:
                ans.append(diff)
                stack.append((temp, diff))
        return reversed(ans)