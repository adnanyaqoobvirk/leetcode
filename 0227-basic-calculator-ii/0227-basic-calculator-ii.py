class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        term = 1
        pop = "*"
        num = 0

        for c in s + "+":
            if c == " ":
                continue
            elif c.isdigit():
                num = num * 10 + int(c)
            elif c == "+" or c == "-":
                if pop == "*":
                    term *= num
                else:
                    term = int(term / num)
                res += term
                num = 0
                term = -1 if c == "-" else 1
                pop = "*"
            else:
                if pop == "*":
                    term *= num
                else:
                    term = int(term / num)
                num = 0
                pop = c
        return res
                
                