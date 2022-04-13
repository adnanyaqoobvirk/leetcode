class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def helper(i: int, j: int, d: str) -> None:
            if i < 0 or j < 0 or i >= n or j >= n or ans[i][j] != 0:
                return
            
            nonlocal counter
            counter += 1
            ans[i][j] = counter
            
            if d == 'u':
                helper(i - 1, j, 'u')
            
            helper(i, j + 1, 'r')
            helper(i + 1, j, 'd')
            helper(i, j - 1, 'l')
            helper(i - 1, j, 'u')
        
        counter = 0
        ans = [[0] * n for _ in range(n)]
        helper(0, 0, 'r')
        return ans