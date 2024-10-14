class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)

        dp = [0] * n
        dp[0] = 1

        count = 0
        for r in range(minJump, n):
            count += dp[r - minJump]
            if r - maxJump > 0:
                count -= dp[r - maxJump - 1]
            
            if s[r] == '0' and count > 0:
                dp[r] = 1
        return dp[-1] == 1
