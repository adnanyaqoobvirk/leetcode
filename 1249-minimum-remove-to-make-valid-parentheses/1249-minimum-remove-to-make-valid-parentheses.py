class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] not in "()":
                continue
                
            if s[i] == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
        
        positions = set(stack)
        ans = []
        for i in range(len(s)):
            if i not in positions:
                ans.append(s[i])
        return "".join(ans)