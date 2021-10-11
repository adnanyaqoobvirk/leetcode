class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        r1, i1 = map(int, num1[:len(num1) - 1].split('+'))
        r2, i2 = map(int, num2[:len(num2) - 1].split('+'))
        
        return f"{r1 * r2 + (-1 * i1 * i2)}+{r1 * i2 + r2 * i1}i"