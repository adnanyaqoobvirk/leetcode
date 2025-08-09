class Solution:
    def soupServings(self, n: int) -> float:
        if n >= 1000:
            return 1

        @cache
        def dp(a, b, p):
            if a <= 0 and b <= 0:
                return p / 2
            if a <= 0 and b > 0:
                return p
            if a <= 0 or b <= 0:
                return 0
            
            res = 0
            for da, db in turns:
                res += dp(a - da, b - db, p * 0.25)
            return res
        turns = [(100, 0), (75, 25), (50, 50), (25, 75)]
        return dp(n, n, 1)
