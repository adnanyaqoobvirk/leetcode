class Solution:
    def numTilings(self, n: int) -> int:
        if n == 1:
            return 1
        
        g, u = [0] * (n + 1), [0] * (n + 1)
        g[1], g[2] = 1, 2
        u[1], u[2] = 1, 2
        for i in range(3, n + 1):
            g[i] = g[i - 1] + g[i - 2] + 2 * u[i - 2]
            u[i] = u[i - 1] + g[i - 1]
            
        return g[n] % (10**9 + 7)