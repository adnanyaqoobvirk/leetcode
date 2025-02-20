class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack:
                return False
            elif c == ")" and stack[-1] != "(":
                return False
            elif c == "}" and stack[-1] != "{":
                return False
            elif c == "]" and stack[-1] != "[":
                return False
            else:
                stack.pop()
        return True