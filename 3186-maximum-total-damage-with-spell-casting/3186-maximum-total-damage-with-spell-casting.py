class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counts = list(Counter(power).items())
        counts.sort()

        n = len(counts)
        dp = [0] * n
        max_damage = 0
        for i in range(n - 1, -1, -1):
            j = bisect_right(counts, (counts[i][0] + 2, inf), i + 1)
            if j == n:
                dp[i] = counts[i][0] * counts[i][1]
            else:
                dp[i] = counts[i][0] * counts[i][1] + dp[j]
            max_damage = max(max_damage, dp[i])
        return max_damage