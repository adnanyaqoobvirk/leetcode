class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = "a", "b"
        if y > x:
            x, y = y, x
            a, b = "b", "a"
        
        stack = []
        res = 0
        for c in chain(s, "$"):
            if c != a and c != b:
                istack = []
                for ic in stack:
                    istack.append(ic)
                    if len(istack) >= 2 and istack[-1] == a and istack[-2] == b:
                        res += y
                        istack.pop()
                        istack.pop()
                stack = []
            else:
                stack.append(c)
                if len(stack) >= 2 and stack[-1] == b and stack[-2] == a:
                    res += x
                    stack.pop()
                    stack.pop()
        return res