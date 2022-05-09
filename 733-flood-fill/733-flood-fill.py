class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image
        
        m, n, stack = len(image), len(image[0]), [(sr, sc)]
        while stack:
            i, j = stack.pop()
            image[i][j] = newColor
            
            for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                if 0 <= x < m and 0 <= y < n and image[x][y] == oldColor:
                    stack.append((x, y))
        return image