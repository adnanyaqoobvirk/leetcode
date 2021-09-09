class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        ans = []
        for c in s:
            if c == ' ':
                while stack:
                    ans.append(stack.pop())
                ans.append(c)
            else:
                stack.append(c)
        while stack:
            ans.append(stack.pop())
        return "".join(ans)