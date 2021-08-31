class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = list(range(1, n + 1))
        while len(teams) > 1:
            m = len(teams) - 1
            teams = [f"({teams[i]},{teams[m - i]})" for i in range((m + 1) // 2)]
        return teams[0]