class Solution:
    def parseTernary(self, e: str) -> str:
        stack, pc = [], ""
        for c in reversed(e):
            if c not in "?:":
                stack.append(c)
                
            if len(stack) >= 3 and pc == "?":
                res = stack[-2] if stack[-1] == 'T' else stack[-3]
                for _ in range(3):
                    stack.pop()
                stack.append(res)
                
            pc = c
        
        if len(stack) > 1:
            return stack[-2] if stack[-1] == 'T' else stack[-3]
        else:
            return stack[-1]