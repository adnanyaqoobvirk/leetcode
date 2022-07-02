class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        prev, curr = [inf], [inf]
        for col in matrix[-1]:
            prev.append(col)
            curr.append(0)
        prev.append(inf)
        curr.append(inf)
        
        for row in reversed(range(n - 1)):
            for col in range(1, n + 1):
                curr[col] = matrix[row][col - 1] + min(
                    prev[col - 1],
                    prev[col],
                    prev[col + 1]
                )
            prev, curr = curr, prev
            
        return min(prev)
        