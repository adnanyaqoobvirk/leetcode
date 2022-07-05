class Solution:
    def numSquares(self, n: int) -> int:
        m = int(sqrt(n)) + 1
        squares = [num**2 for num in range(1, m)]
        
        curr = [inf] * (n + 1)
        curr[0] = 0
        for remaining in range(1, n + 1):
            for i in range(int(sqrt(remaining))):
                curr[remaining] = min(
                    curr[remaining], 1 + curr[remaining - squares[i]]
                )
        return curr[n]