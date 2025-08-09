class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 10000:
            return 1

        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0 and b > 0:
                return 1
            if a <= 0 or b <= 0:
                return 0
            
            res = 0
            for da, db in turns:
                res += dp(a - da, b - db)
            return res * 0.25
        turns = [(100, 0), (75, 25), (50, 50), (25, 75)]
        return dp(n, n)
