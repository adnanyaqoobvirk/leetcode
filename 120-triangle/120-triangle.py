class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        
        prev = triangle[-1][::]
        curr = [0] * (len(triangle[-1]) - 1)
        for row in reversed(range(n - 1)):
            for col in range(row + 1):
                curr[col] = triangle[row][col] + min(
                    prev[col],
                    prev[col + 1]
                )
            prev, curr = curr, [0] * row
        return prev[0]
    
        