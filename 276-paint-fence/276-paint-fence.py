class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        
        prev, curr = k, k * k
        for i in range(3, n + 1):
            prev, curr = curr, (k - 1) * (curr + prev)
        return curr