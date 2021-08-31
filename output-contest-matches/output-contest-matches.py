class Solution:
    def findContestMatch(self, n: int) -> str:
        teams = list(range(1, n + 1))
        while len(teams) > 1:
            start, end = 0, len(teams) - 1
            new_teams = []
            while start < end:
                new_teams.append(f"({teams[start]},{teams[end]})")
                start += 1
                end -= 1
            teams = new_teams
        return teams[0]