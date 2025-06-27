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
            else:
                term = term * num if pop == "*" else int(term / num)
                num = 0

                if c == "+" or c == "-":
                    res += term
                    term = -1 if c == "-" else 1
                    pop = "*"
                else:
                    pop = c
        return res
                
                