class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        score = (1 << w - 1) * h
        for j in range(1, w):
            ones = sum(grid[i][0] == grid[i][j] for i in range(h))
            score += (1 << w - j - 1) * max(ones, h - ones)
        return score