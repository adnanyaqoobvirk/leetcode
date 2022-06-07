class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        prev = [matrix[n - 1][j] for j in range(n)]
        prev.append(float('inf'))
        curr = [float('inf')] * (n + 1)
            
        for i in reversed(range(n - 1)):
            for j in reversed(range(n)):
                curr[j] = matrix[i][j] + min(
                    prev[j - 1],
                    prev[j],
                    prev[j + 1]
                )
            prev, curr = curr, prev
        return min(prev)