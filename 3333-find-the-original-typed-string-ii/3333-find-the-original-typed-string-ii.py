class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        groups = []
        start = 0
        for end in range(1, len(word)):
            if word[start] != word[end]:
                groups.append(end - start)
                start = end
        groups.append(len(word) - start)
        
        total = 1
        for g in groups:
            total = (total * g) % MOD

        if k <= len(groups):
            return total

        dp = [0] * k
        dp[0] = 1

        for g in groups:
            new_dp = [0] * k
            curr = 0
            for j in range(1, k):
                curr = (curr + dp[j - 1])
                
                if j > g:
                    curr = (curr - dp[j - g - 1])
                
                new_dp[j] = curr
            dp = new_dp
        return (total - sum(dp)) % MOD