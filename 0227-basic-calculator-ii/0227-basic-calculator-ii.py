class Solution:
    def calculate(self, s: str) -> int:
        def split(expr: str) -> List[str]:
            res = []
            num = []
            for c in s:
                if c == " ":
                    continue
                elif c.isdigit():
                    num.append(c)
                else:
                    if num:
                        res.append("".join(num))
                        num = []
                    res.append(c)
            if num:
                res.append("".join(num))
            return res
        
        def postfix(ops: List[str]) -> List[str]:
            operators = {"+": 1, "-": 1, "*": 2, "/": 2}
            stack = []
            res = []
            for op in ops:
                if op in operators:
                    while stack and operators.get(stack[-1]) >= operators[op]:
                        res.append(stack.pop())
                    stack.append(op)
                else:
                    res.append(op)
            while stack:
                res.append(stack.pop())
            return res
        
        def evaluate(ops: List[str]) -> int:
            stack = []
            for op in ops:
                if op.isdigit():
                    stack.append(int(op))
                else:
                    opnd2, opnd1 = stack.pop(), stack.pop()
                    if op == "+":
                        stack.append(opnd1 + opnd2)
                    elif op == "-":
                        stack.append(opnd1 - opnd2)
                    elif op == "*":
                        stack.append(opnd1 * opnd2)
                    else:
                        stack.append(opnd1 // opnd2)
            return stack[-1]

        tokens = split(s)
        operations = postfix(tokens)
        return evaluate(operations)