class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n, m = len(image), len(image[0])
        mini, maxi = n - 1, 0
        minj, maxj = m - 1, 0
        for i in range(n):
            for j in range(m):
                if image[i][j] == '1':
                    mini, maxi = min(mini, i), max(maxi, i)
                    minj, maxj = min(minj, j), max(maxj, j)
        return (maxi - mini + 1) * (maxj - minj + 1)