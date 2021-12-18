class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        nstr = str(n) 
        dp = [0] * (len(nstr) + 1)
        dp[-1] = 1
        for i in reversed(range(len(nstr))):
            num = int(nstr[i])
            for d in digits:
                if int(d) < num:
                    dp[i] += len(digits) ** (len(nstr) - i - 1)
                elif int(d) == num:
                    dp[i] += dp[i + 1]
        return dp[0] + sum(len(digits) ** i for i in range(1, len(nstr)))