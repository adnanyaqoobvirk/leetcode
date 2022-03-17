class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        n, i, stack = len(s), 0, [0]
        while i < n:
            if s[i] == '(':
                if s[i + 1] == ')':
                    stack[-1] += 1
                    i += 1
                else:
                    stack.append(0)
            else:
                if s[i - 1] != '(':
                    score = 2 * stack.pop()
                    stack[-1] += score
            i += 1
        return stack[0]