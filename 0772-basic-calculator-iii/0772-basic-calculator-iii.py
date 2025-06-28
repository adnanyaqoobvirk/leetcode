class Solution:
    def calculate(self, s: str) -> int:
        def evaluate(op1: int, opr: str, op2: int) -> int:
            if opr == "+":
                return op1 + op2
            elif opr == "-":
                return op1 - op2
            elif opr == "*":
                return op1 * op2
            else:
                return int(op1 / op2)
        
        ops = {"+": 1, "-": 1, "*": 2, "/": 2}
        stack = ["("]
        num = 0
        for c in chain(s, ")"):
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                stack.append(c)
            elif c in ops:
                while stack and stack[-1] != "(" and ops.get(stack[-1], 0) >= ops[c]:
                    opr, op1 = stack.pop(), stack.pop()
                    num = evaluate(op1, opr, num)
                stack.append(num)
                stack.append(c)
                num = 0
            elif c == ")":
                while stack and stack[-1] != "(":
                    opr, op1 = stack.pop(), stack.pop()
                    num = evaluate(op1, opr, num)
                stack.pop()
        return num