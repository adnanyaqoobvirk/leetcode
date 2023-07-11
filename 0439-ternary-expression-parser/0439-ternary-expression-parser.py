class Solution:
    def parseTernary(self, e: str) -> str:
        stack = []
        for c in reversed(e):
            if len(stack) >= 4 and stack[-2] == "?":
                res = stack[-3] if stack[-1] == 'T' else stack[-4]
                for _ in range(4):
                    stack.pop()
                stack.append(res)
            if c != ":":
                stack.append(c)
        
        if len(stack) > 1:
            return stack[-3] if stack[-1] == 'T' else stack[-4]
        else:
            return stack[-1]