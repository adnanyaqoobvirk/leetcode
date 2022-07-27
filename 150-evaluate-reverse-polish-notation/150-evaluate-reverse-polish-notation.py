class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        specials = {'+','-','*','/'}
        
        stack = []
        for token in tokens:
            if token not in specials:
                stack.append(int(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(a / b))
        return stack[-1]