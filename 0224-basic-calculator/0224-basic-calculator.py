class Solution:
    def calculate(self, s: str) -> int:
        digits = set("1234567890")
        
        stack = []
        i = len(s)
        while i > 0:
            i -= 1
            c = s[i]
            if c == ' ':
                continue
            elif c == ')' or c == '+' or c == '-':
                stack.append(c)
            elif c == '(':
                r = 0
                sign = 1
                while stack and stack[-1] != ')':
                    t = stack.pop()
                    if t == '-':
                        sign = -1
                    elif t == '+':
                        sign = 1
                    else:
                        r += sign * t
                stack.pop()
                stack.append(r)
            else:
                num = 0
                j = 0
                while i >= 0 and s[i] in digits:
                    num = int(s[i]) * 10**j + num
                    i -= 1
                    j += 1
                stack.append(num)
                i += 1
        r = 0
        sign = 1
        while stack:
            t = stack.pop()
            if t == '-':
                sign = -1
            elif t == '+':
                sign = 1
            else:
                r += sign * t
        return r