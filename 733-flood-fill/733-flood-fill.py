class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        q, nimage, visited = [(sr, sc)], [row[:] for row in image], {(sr, sc)}
        nimage[sr][sc] = newColor
        while q:
            nq = []
            for i, j in q:
                for x, y in [(i, j - 1), (i, j + 1), (i - 1, j), (i + 1, j)]:
                    if 0 <= x < m and 0 <= y < n and (x, y) not in visited and image[x][y] == image[sr][sc]:
                        visited.add((x, y))
                        nimage[x][y] = newColor
                        nq.append((x, y))
            q = nq
        return nimage