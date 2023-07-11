class Solution:
    def parseTernary(self, e: str) -> str:
        stack = []
        for c in reversed(e):
            if len(stack) >= 5 and stack[-2] == "?" and stack[-4] == ":":
                res = stack[-3] if stack[-1] == 'T' else stack[-5]
                for _ in range(5):
                    stack.pop()
                stack.append(res)
            stack.append(c)
        
        if len(stack) > 1:
            return stack[-3] if stack[-1] == 'T' else stack[-5]
        else:
            return stack[-1]