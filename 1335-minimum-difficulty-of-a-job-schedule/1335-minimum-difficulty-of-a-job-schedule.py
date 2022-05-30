class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        
        dp = [[0] * d for _ in range(n)]
        dp.append([float('inf')] * d)
        for pos in reversed(range(n)):
            dp[pos][0] = max(jobDifficulty[pos:])
            
        for day in range(1, d):
            for pos in reversed(range(n)):
                total_difficulty = float('inf')
                day_difficulty = 0
                for i in range(pos, n):
                    day_difficulty = max(day_difficulty, jobDifficulty[i])
                    total_difficulty = min(
                        total_difficulty,
                        day_difficulty + dp[i + 1][day - 1]
                    )
                dp[pos][day] = total_difficulty
        return -1 if dp[0][d - 1] == float('inf') else dp[0][d - 1]
            