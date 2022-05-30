class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        @cache
        def helper(pos: int, day: int) -> int:
            if day == 0:
                return max(jobDifficulty[pos:]) if pos < n else 0
            
            if pos >= n:
                return float('inf')

            total_difficulty = float('inf')
            day_difficulty = 0
            for i in range(pos, n):
                day_difficulty = max(day_difficulty, jobDifficulty[i])
                total_difficulty = min(
                    total_difficulty,
                    day_difficulty + helper(i + 1, day - 1)
                )
            return total_difficulty
        
        n = len(jobDifficulty)
        ans = helper(0, d)
        return -1 if ans == float('inf') else ans