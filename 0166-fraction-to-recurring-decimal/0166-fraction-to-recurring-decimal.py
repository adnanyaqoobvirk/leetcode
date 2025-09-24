class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
            
        if numerator < 0 and denominator >= 1:
            return "-" + self.fractionToDecimal(-numerator, denominator)
        elif numerator >= 0 and denominator < 0:
            return "-" + self.fractionToDecimal(numerator, -denominator)
        elif numerator < 0 and denominator < 0:
            return self.fractionToDecimal(-numerator, -denominator)

        whole, remainder = divmod(numerator, denominator)
        seen = {}
        fractional = []
        while remainder != 0 and remainder not in seen:
            seen[remainder] = len(fractional)
            if remainder < denominator:
                remainder *= 10
            digit, remainder = divmod(remainder, denominator)
            fractional.append(str(digit))
        if remainder != 0:
            fractional.insert(seen[remainder], "(")
            fractional.append(")")
        
        ans = [str(whole)]
        if len(fractional) >= 1:
            ans.append(".")
            ans.extend(fractional)
        return "".join(ans)