class Solution:
    def calculate(self, s: str) -> int:
        DIGITS = set("1234567890")
        
        def calc_sub_expr():
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
            return r
        
        def get_num():
            nonlocal i
            
            num = j = 0
            while i >= 0 and s[i] in DIGITS:
                num = int(s[i]) * 10**j + num
                i -= 1
                j += 1
            i += 1
            return num
        
        stack, i = [], len(s)
        while i > 0:
            i -= 1
            c = s[i]
            
            if c == ' ':
                continue
            elif c == ')' or c == '+' or c == '-':
                stack.append(c)
            elif c == '(':
                r = calc_sub_expr()
                stack.pop()
                stack.append(r)
            else:
                stack.append(get_num())
        return calc_sub_expr()