class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def helper() -> int:
            token = next(itr)
            if token in "+-*/":
                second, first = helper(), helper()
                if token == "+":
                    return first + second
                elif token == "-":
                    return first - second
                elif token == "*":
                    return first * second
                else:
                    return int(first / second)
            else:
                return int(token)
        itr = iter(reversed(tokens))
        return helper()