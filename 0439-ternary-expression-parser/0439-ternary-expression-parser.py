class Solution:
    def parseTernary(self, e: str) -> str:
        stack, i = [], len(e) - 1
        while i >= 1:
            if e[i] == "?":
                if e[i - 1] == "T":
                    res = stack.pop()
                    stack.pop()
                    stack.append(res)
                else:
                    stack.pop()
                i -= 1
            elif e[i] != ":":
                stack.append(e[i])
            i -= 1
        return stack[0]