class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        n, m = len(image), len(image[0])
        
        mini, maxi = n - 1, 0
        minj, maxj = m - 1, 0
        
        stack = [(x, y)]
        while stack:
            i, j = stack.pop()
            
            mini, maxi = min(mini, i), max(maxi, i)
            minj, maxj = min(minj, j), max(maxj, j)
            image[i][j] = "0"
            
            if i - 1 >= 0 and image[i - 1][j] == '1':
                stack.append((i - 1, j))
            
            if i + 1 < n and image[i + 1][j] == '1':
                stack.append((i + 1, j))
            
            if j - 1 >= 0 and image[i][j - 1] == '1':
                stack.append((i, j - 1))
            
            if j + 1 < m and image[i][j + 1] == '1':
                stack.append((i, j + 1))
            
        return (maxi - mini + 1) * (maxj - minj + 1)