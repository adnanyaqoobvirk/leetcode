class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort(key=lambda x: x[0])

        fpositions = []
        for f, l in factory:
            fpositions.extend([f] * l)
            
        n, m = len(robot), len(fpositions)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][m] = inf

        for i in reversed(range(n)):
            for j in reversed(range(m)):
                dp[i][j] = min(
                    abs(robot[i] - fpositions[j]) + dp[i + 1][j + 1],
                    dp[i][j + 1]
                )
        return dp[0][0]