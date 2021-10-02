class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon) - 1, len(dungeon[0]) - 1
        dp = [[float('inf')] * (m + 2) for _ in range(n + 2)]
        
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    dp[i][j] = -dungeon[i][j] + 1 if dungeon[i][j] < 0 else 1
                else:
                    health = min(
                        dp[i + 1][j],
                        dp[i][j + 1]
                    ) - dungeon[i][j]
                    dp[i][j] = 1 if health <= 0 else health
        return dp[0][0]