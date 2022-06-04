class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 2)
        dp[n] = 1
        for pos in reversed(range(n)):
            count = 0
            if s[pos] != '0':
                count += dp[pos + 1]
            
            if pos < n - 1 and 10 <= int(f"{s[pos]}{s[pos + 1]}") <= 26:
                count += dp[pos + 2]
            dp[pos] = count
        return dp[0]