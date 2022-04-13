class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        n2 = n * n
        num = 0
        a, b, c, d = 0, 0, n - 1, n - 1
        ans = [[None] * n for _ in range(n)]
        while num < n2:
            i = a
            for j in range(b, d + 1):
                num += 1
                ans[i][j] = num
            
            i += 1
            for i in range(i, c + 1):
                num += 1
                ans[i][j] = num
            
            for j in reversed(range(b, d)):
                num += 1
                ans[i][j] = num
            
            for i in reversed(range(a + 1, c)):
                num += 1
                ans[i][j] = num
            
            a, b, c, d = a + 1, b + 1, c - 1, d - 1
        return ans