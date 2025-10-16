class Solution:
    def cheapestJump(self, coins: List[int], maxJump: int) -> List[int]:
        n = len(coins)
        parent = [-1] * n
        dp = [inf] * n
        dp[-1] = coins[-1]
        parent[-1] = n - 1
        for i in reversed(range(n - 1)):
            if coins[i] == -1:
                continue

            for j in range(i + 1, min(i + maxJump + 1, n)):
                if coins[j] == -1:
                    continue
                
                if dp[j] + coins[i] < dp[i]:
                    dp[i] = dp[j] + coins[i]
                    parent[i] = j
        
        ans = [1]
        i = 0
        while i < n - 1:
            i = parent[i]
            if i == -1:
                return []
            ans.append(i + 1)
        return ans