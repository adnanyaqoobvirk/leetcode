class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @cache
        def helper(x: int, y: int, moves: int) -> int:
            if moves == maxMove:
                return 0
            
            ans = 0
            for i, j in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if 0 <= i < m and 0 <= j < n:
                    ans += helper(i, j, moves + 1)
                else:
                    ans += 1
            return ans % MOD
        
        MOD = 10**9 + 7
        return helper(startRow, startColumn, 0)