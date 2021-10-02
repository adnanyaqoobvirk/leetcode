class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon) - 1, len(dungeon[0]) - 1

        prev_row = [float('inf')] * (m + 2)
        curr_row = [float('inf')] * (m + 2)
        for i in range(n, -1, -1):
            for j in range(m, -1, -1):
                if i == n and j == m:
                    curr_row[j] = -dungeon[i][j] + 1 if dungeon[i][j] < 0 else 1
                else:
                    health = min(
                        prev_row[j],
                        curr_row[j + 1]
                    ) - dungeon[i][j]
                    curr_row[j] = 1 if health <= 0 else health
            prev_row, curr_row = curr_row, prev_row
        return prev_row[0]