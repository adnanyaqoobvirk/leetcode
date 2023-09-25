class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev, curr = [0] * 100, [0] * 100
        prev[0] = poured
        for i in range(1, query_row + 1):
            for j in range(i + 1):
                curr[j] = max(0, prev[j] - 1) / 2 + max(0, prev[j - 1] - 1) / 2
            prev, curr = curr, prev
        return min(1, prev[query_glass])