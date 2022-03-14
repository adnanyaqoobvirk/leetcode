class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if newColor == oldColor:
            return image
        
        def helper(i: int, j: int) -> None:
            image[i][j] = newColor
            for x, y in [(i, j - 1), (i, j + 1), (i + 1, j), (i - 1, j)]:
                if 0 <= x < n and 0 <= y < m and image[x][y] == oldColor:
                    helper(x, y)
        n, m = len(image), len(image[0])
        helper(sr, sc)
        return image