class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opr, stack = {"+", "-", "*", "/"}, []
        for t in tokens:
            if t in opr:
                s, f = int(stack.pop()), int(stack.pop())
                
                if t == "+":
                    stack.append(f + s)
                elif t == "-":
                    stack.append(f - s)
                elif t == "*":
                    stack.append(f * s)
                else:
                    stack.append(f / s)
            else:
                stack.append(t)
        return int(stack[0])