class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i, c in enumerate(s):
            if c == ')':
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append((c, i))
            elif c == '(':
                stack.append((c, i))
        
        ans, j = [], 0
        for i, c in enumerate(s):
            if j < len(stack) and i == stack[j][1]:
                j += 1
                continue
            else:
                ans.append(c)
        return "".join(ans)